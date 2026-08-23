class DataPipeline:
    SUPPORTED_FORMATS = ("CSV", "PARQUET", "JSON")
    __log_history = None

    @classmethod
    def get_supported_formats(cls) -> tuple:
        return cls.SUPPORTED_FORMATS

    @staticmethod
    def clean_string(text):
        clean_text = text.strip().upper()
        return clean_text

    @staticmethod
    def get_log_history():
        if DataPipeline.__log_history is None:
            DataPipeline.__log_history = []
        return DataPipeline.__log_history

if __name__ == "__main__":
    print("SUPPORTED FORMATS:" , DataPipeline.get_supported_formats())
    raw_text = "    data_science_project      "
    print("Clean text:", DataPipeline.clean_string(raw_text))

    # Test Static Method: Singleton log history
    log1 = DataPipeline.get_log_history()
    log1.append("Pipeline started at 10:00 AM")

    log2 = DataPipeline.get_log_history()
    log2.append("Processed 1000 rows")

    # Kiểm tra log2 có chứa cả dữ liệu của log1 không (chứng minh cùng 1 đối tượng)
    print("Log History:", log2)