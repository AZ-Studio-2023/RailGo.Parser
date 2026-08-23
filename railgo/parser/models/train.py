class TrainModel(object):
    '''客运列车数据结构'''
    number = ""
    numberFull = []
    numberKind = ""
    code = ""
    type = ""
    diagramType = ""

    bureau = ""
    bureauName = ""
    runner = ""
    carOwner = ""
    car = ""

    diagram = []
    timetable = []
    spend = 0
    rundays = []
    route = []

    isFuxing = False
    isReconnection = False

    _beginDay = ""
    _dataBeginDay = ""

    def toJson(self):
        return {
            "number": self.number,
            "numberFull": self.numberFull,
            "numberKind": self.numberKind,
            "code": self.code,
            "bureau": self.bureau,
            "bureauName": self.bureauName,
            "type": self.type,
            "diagramType": self.diagramType, 
            "diagram": self.diagram,
            "rundays": self.rundays,
            "route": self.route,
            "runner": self.runner,
            "carOwner": self.carOwner,
            "car": self.car,
            "timetable": self.timetable,
            "spend": self.spend,
            "isFuxing": self.isFuxing
        }

    @classmethod
    def fromJson(self, json_data):
        train = self()
        field_mapping = {
            "number": "number",
            "numberFull": "numberFull",
            "numberKind": "numberKind",
            "code": "code",
            "type": "type",
            "diagramType": "diagramType",
            "bureau": "bureau",
            "bureauName": "bureauName",
            "runner": "runner",
            "carOwner": "carOwner",
            "car": "car",
            "diagram": "diagram",
            "timetable": "timetable",
            "spend": "spend",
            "rundays": "rundays",
            "route": "route",
            "isFuxing": "isFuxing"
        }
        
        for json_key, attr_name in field_mapping.items():
            if json_key in json_data:
                setattr(train, attr_name, json_data[json_key])

        return train

    def __hash__(self):
        '''根据TrainCode分辨列车，避免一车多号导致缺少信息'''
        return hash(self.code)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.code == other.code
        return False
