class PostgreSQLDatabase:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.connection_status = "Connected"

    def fetch_data(self, query: str) -> list[dict]:
        print(f"Đang kết nối tới {self.db_url} để lấy dữ liệu...")
        return [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Mouse"}]

    def close_connection(self):
        print("Đã đóng kết nối Database")

class PDFReportExporter:
    def __init__(self, database: PostgreSQLDatabase):
        self.database = database

    def export(self, query: str, file_path: str):
        data = self.database.fetch_data(query) #Nghĩa là gọi sql.fetch_data("A")
        print(f"Đang xuất {len(data)} bản ghi ra file PDF tại: {file_path}")

if __name__ == "__main__":
    sql = PostgreSQLDatabase("máy chủ") #Nghĩa là self.database = sql, và sql.db_url = "máy chủ"
    pdf = PDFReportExporter(sql)
    pdf.export("A", "B")
    #Output:
    # Đang kết nối tới máy chủ để lấy dữ liệu...
    #Đang xuất 2 bản ghi ra file PDF tại: B 
    #(2 là do ở hàm return chỗ fetch_data)