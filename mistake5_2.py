from dataclasses import dataclass
from typing import Protocol

class ReadableConfig(Protocol):
    def read(self, key: str) -> str: ...
        
class WritableConfig(Protocol):
    def write(self, key: str, value: str) -> None: ...

@dataclass(frozen=True)
class DefaultConfigFile:
    data: dict

    def read(self, key: str) -> str:
        return self.data.get(key, "")
    #Cơ chế tạo bản sao mới
    def with_updated_key(self, key: str, value: str) -> "DefaultConfigFile":
        new_data = {**self.data, key: value} #Cú pháp ngắn gọn cập nhật
        return DefaultConfigFile(data=new_data)

class WritableConfigFile:
    def __init__(self, data: dict):
        self.data = data
    def read(self, key: str) -> str:
        return self.data.get(key, "")
    #Sửa trực tiếp
    def write(self, key: str, value: str) -> None:
        self.data[key] = value

if __name__ == "__main__":
    d1 = DefaultConfigFile(data={"theme": "dark", "caidat": "riengtu"})
    print(d1.read("caidat")) #riengtu
    print(d1.with_updated_key("caidai", "congkhai")) #DefaultConfigFile(data={'theme': 'dark', 'caidat': 'riengtu', 'caidai': 'congkhai'})
    print()

    d2 = WritableConfigFile(data={"theme": "dark", "caidat": "riengtu"})
    d2.write("caidat", "congkhai")
    print(d2.read("caidat")) #congkhai