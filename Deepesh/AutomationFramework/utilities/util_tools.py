import json
import openpyxl
# command to install module
# -> pip install openpyxl

class Utils:

    def read_json_data(self, file_path):
        with open(file_path, "r") as file:
            data = file.read()
            json_data = json.loads(data)
        return json_data

    def read_excel_file(self, file_path, sheet_name, cell_name):
        wb = openpyxl.load_workbook(file_path)
        sheet = wb[sheet_name]
        cell = sheet[cell_name]
        return cell.value


if __name__ == '__main__':
    obj = Utils()
    data = obj.read_json_data("sample_data.json")
    print(data)
    print(data['Admin']['user_role'])