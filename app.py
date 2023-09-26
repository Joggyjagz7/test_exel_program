import pandas as pd
import streamlit as st

def upload_excel_as_sheet(input_file, target_file, sheet_name):
    # Read the source Excel file
    source_df = pd.read_excel(input_file)

    # Load the target Excel workbook
    target_excel = pd.ExcelWriter(target_file, engine='openpyxl')
    target_excel.book = target_excel.book

    # Write the source DataFrame to the target workbook as a new sheet
    source_df.to_excel(target_excel, sheet_name=sheet_name, index=False)

    # Save the target workbook
    target_excel.save()
    st.success(f"Uploaded '{input_file}' as '{sheet_name}' in '{target_file}'")

def main():
    st.title("Excel Sheet Uploader")

    # File upload widget
    input_file = st.file_uploader("Upload Source Excel File", type=["xlsx", "xls"])

    if input_file is not None:
        target_file = "https://github.com/Joggyjagz7/test_exel_program/blob/main/Main%20sheet.xlsx"  # Replace with your target Excel file path

        # Sheet name input
        sheet_name = st.text_input("Enter Sheet Name", "NewSheet")

        # Upload button
        if st.button("Upload"):
            upload_excel_as_sheet(input_file, target_file, sheet_name)

if __name__ == "__main__":
    main()
