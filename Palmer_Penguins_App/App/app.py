"""
====================
Palmer Penguins App
====================

--- Instructions ---
    1)  Execute "source .venv_shiny/bin/activete" to activate the virtual environment required to run this app.
    2)  Execute "shiny run app.py --reload".

--- Output(s) ---
    -   A Shiny app.
"""

# region: --- Modules ---

from shiny import App, render, ui, reactive # The "reactive" module allows for reactive calculations.
import pandas as pd
from plotnine import ggplot, geom_density, aes, theme_light

# endregion (Data Umbrella, 2023)

# region: --- UI Component ---

# Use a fluid page layout.
app_ui = ui.page_fluid(
    # Add a sidebar layout.
    ui.layout_sidebar(
        # Add a sidebar panel.
        ui.panel_sidebar(            
            # Add an input slider.
            ui.input_slider(id='mass', label='Max Body Mass', min=2000, max=8000, value=2000),
            # Add an input action button.
            ui.input_action_button(id='reset', label='Reset Filter')
        ),
        # Add a main panel.
        ui.panel_main(
            # Add a table as the server function's output in the main panel.
            ui.output_table('summary'),
            # Also add a histogram as the server function's output in the main panel.
            ui.output_plot('histogram')
        )
    )
)

# endregion (Data Umbrella, 2023)

# region: --- Server Component ---

# Define a function for the server component. The code inside the "server()" function runs whenever the user initially loads the application.
def server(input, output, session):

    # Define the absolute path to the "penguins.csv" file.
    abs_path_penguins = '/mnt/c/Users/ajauw/OneDrive/Documents/3P/W/Programming/Python/Projects/Palmer_Penguins_App/penguins.csv' # Change this path to the absolute path to the file stored in your local machine.

    # Read the "penguins.csv" file.
    penguins = pd.read_csv(abs_path_penguins) # The file is read outside the functions below to increase code efficiency, since the code does not have to re-read the "penguins.csv" file every time the user changes the input.

    # Tell Shiny to perform reactive calculations on the function below.
    @reactive.Calc
    # Define a function that filters the data in the "penguins.csv" file.
    def data_filterer():
        # Copy the "penguins.csv" file to prevent the original file from being altered.
        df_penguins = penguins.copy()
        # Only display rows in the "df_penguins" DataFrame containing body masses greater than what the user inputs via the "ui.input_slider" function above.
        df_penguins = df_penguins.loc[df_penguins['body_mass_g'] > input.mass()]
        # Return the "df_penguins" DataFrame.
        return df_penguins

    # Tell Shiny to induce a reactive effect on the function below.
    @reactive.Effect
    # Tell Shiny the event to which it should respond with a reactive effect.
    @reactive.event(input.reset)
    # Define a function that induces a reactive effect. "_" is the naming convention for a reactive effect function.
    def _():
        # Reset the input slider.
        ui.update_slider(id='mass', value=2000)

    # Tell Shiny the function below is an output. The code inside the "output" decorator runs every time the user changes the input.
    @output
    # Tell Shiny the output will be a table.
    @render.table
    # Define a function for the "summary" id, called in the "ui.output_table()" function above.
    def summary():
        # Filter the data in the "penguins.csv" file using the "data_filterer()" function.
        df_penguins_filt = data_filterer()
        # Group the displayed rows by species (forming column 1 of a DataFrame), then display the number of individuals with body masses above what the user inputs (forming column 2 of the DataFrame).
        df_penguins_filt = df_penguins_filt.groupby('species', as_index=False).size()
        # Return the "df_penguins" DataFrame.
        return df_penguins_filt

    # Tell Shiny the function below is another output.
    @output
    # Tell Shiny the output will be a plot.
    @render.plot
    # Define a function for the "histogram" id, called in the "ui.output_plot()" function above.
    def histogram():
        # Filter the data in the "penguins.csv" file using the "data_filterer()" function.
        df_hist_penguins_filt = data_filterer()
        # Create a histogram called "hist_penguins", showing the frequency of individuals with body masses greater than what the user inputs and grouped by species.
        hist_penguins_filt = (
            ggplot(df_hist_penguins_filt, aes(x='body_mass_g', fill='species')) +
            geom_density(alpha=0.2) +
            theme_light()
        )
        # Return the "hist_penguins" histogram.
        return hist_penguins_filt

# endregion (Data Umbrella, 2023)

# region: --- App ---

app = App(app_ui, server)

# endregion (Data Umbrella, 2023)

# region: --- References ---

# Data Umbrella. (2023, May 9). [79] Create a Python web app using Shiny (Gordon Shotwell) [Video]. YouTube. https://www.youtube.com/watch?v=pXidQWYY14w&t=524s&ab_channel=DataUmbrella

# endregion
