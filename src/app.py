from frontend import ExcelValidadorUI
from backend import process_excel, excel_to_sql
#import logging
#import sentry_sdk


def main():
    ui = ExcelValidadorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        df, result, error = process_excel(upload_file)
        ui.display_results(result, error)

        if error:
            ui.display_wrong_message()
            logging.error("Planilha apresentava erro de schema")
            sentry_sdk.capture_message("A planilha Excel estava errada")
        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_success_message()
            logging.info(" Foi enviado com sucesso o banco SQL")
            sentry_sdk.capture_message("O banco SQL foi atualizado")

if __name__ == "__main__":
    main()