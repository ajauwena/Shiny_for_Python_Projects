"""
====================================
Insurance Premium Data Explorer App
====================================

--- Instructions ---
    -   See "master_script.py".

--- Output(s) ---
    -   A Shiny app.
"""

# region: --- To-Do ---

#   1.  Add comments.

# endregion

# region: --- Importing Modules ---

from shiny import App, render, ui, reactive
import pandas as pd
from plotnine import ggplot, geom_histogram, aes, theme_light

# endregion

# region: --- Initializing Variables ---

df_insurance = pd.read_csv('insurance_dataset.csv', header=0, encoding="utf8")

col_names_insurance = df_insurance.columns.tolist()

# endregion

# region: --- UI Component ---

# Create a fluid page.
app_ui = ui.page_fluid(
    # Create a title for the application.
    ui.panel_title('Insurance Premium Data Explorer'),
    # Create a sidebar layout component.
    ui.layout_sidebar(
        # Create a sidebar element.
        ui.sidebar(
            ui.input_select(id='variable_select', label='Select a variable:', choices=col_names_insurance, selected='age'),
            ui.output_text(id='selected_variable')
            ),
        ui.output_plot(id='visualization')
    )
)

# endregion

# region: --- Server Component ---

# Define a server function.
def server(input, output, session):

    @output
    @render.text
    def selected_variable():
        return f'You selected {input.variable_select()}.'

    @output
    @render.plot
    def visualization():
        selected_variable_insurance = input.variable_select()
        hist_selected_variable_insurance = ( # Add a "binwidth" argument.
            ggplot(df_insurance, aes(x=selected_variable_insurance)) +
            geom_histogram() +
            theme_light()
        )
        return hist_selected_variable_insurance

# endregion

# region: --- App ---

app = App(app_ui, server)

# endregion

# region: --- Example ---

#app_ui = ui.page_fluid(
    #ui.panel_title("Hello Shiny!"),
    #ui.input_slider("n", "N", 0, 100, 20),
    #ui.output_text_verbatim("txt"),
#)


#def server(input, output, session):
    #@render.text
    #def txt():
        #return f"n*2 is {input.n() * 2}"


#app = App(app_ui, server)

# endregion