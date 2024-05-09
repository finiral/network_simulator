class Site :
    _domaine:str
    def setDomaine(self,domaine:str):
        self._domaine=domaine
    def getDomaine(self):
        return self._domaine
    
    def __init__(self,domaine:str):
        self.setDomaine(domaine)