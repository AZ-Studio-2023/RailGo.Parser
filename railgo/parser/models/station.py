class StationModel(object):
    bureau = ""
    belong = ""
    name = ""
    tmism = "未知"
    tmismAlias = []
    level = "未知"
    telecode = ""
    telecodeAlias = []
    pinyin = ""
    pinyinTriple = ""
    lines = []
    type = []  # 货 客 高 行 运
    province = ""
    city = ""
    trainList = []
    sameCityStationList = []

    def toJson(self):
        return {
            "name": self.name,
            "tmism": self.tmism,
            "tmismAlias": self.tmismAlias,
            "level": self.level,
            "telecode": self.telecode,
            "telecodeAlias": self.telecodeAlias,
            "pinyin": self.pinyin,
            "pinyinTriple": self.pinyinTriple,
            "bureau": self.bureau,
            "belong": self.belong,
            "province": self.province,
            "city": self.city,
            "sameCityStationList": self.sameCityStationList,
            "lines": self.lines,
            "type": self.type,
            "trainList": self.trainList
        }

    @classmethod
    def fromJson(self, json_data):
        station = self()
        
        field_mapping = {
            "name": "name",
            "tmism": "tmism",
            "tmismAlias": "tmismAlias",
            "level": "level",
            "telecode": "telecode",
            "telecodeAlias": "telecodeAlias",
            "pinyin": "pinyin",
            "pinyinTriple": "pinyinTriple",
            "bureau": "bureau",
            "belong": "belong",
            "province": "province",
            "city": "city",
            "sameCityStationList": "sameCityStationList",
            "lines": "lines",
            "type": "type",
            "trainList": "trainList"
        }
        
        for json_key, attr_name in field_mapping.items():
            if json_key in json_data:
                setattr(station, attr_name, json_data[json_key])
        
        return station

    def __hash__(self):
        return hash(self.tmism+self.telecode)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.tmism + self.telecode == other.tmism+other.telecode
        return False
