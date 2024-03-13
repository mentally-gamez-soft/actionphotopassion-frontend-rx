

class ServiceClassManager:

    cache:dict = {} 
    
    def add_target_cache_to_cache_inventory(self,cache_key:str):
        self.cache[cache_key] = []

    def __retrieve_cache_value__(self,cache_key:str) -> list:
        return self.cache.get(cache_key)

    def __exists_id_in_cache__(self, cache_key:str, id:int) -> dict:        
        targeted_cache = self.__retrieve_cache_value__(cache_key)

        if targeted_cache:
            element = [obj for obj in targeted_cache if obj.get_id() == id]
            return {"status":len(element) > 0, "obj":element[:]}
        return {"status":False, "obj":None}
    
    def __exists_obj_in_cache__(self, cache_key:str, obj_reader:ObjectParser) -> bool:
        targeted_cache = self.__retrieve_cache_value__(cache_key)
        
        if targeted_cache:
            element = [obj for obj in targeted_cache if obj.get_id() == obj_reader.get_id()]
            return len(element) > 0
        return True

    def add_to_cache(self, cache_key:str, obj_reader:ObjectParser):
        if not self.__exists_obj_in_cache__(cache_key, obj_reader):
            self.cache[cache_key].append(obj_reader)

    def get_from_cache(self, cache_key:str, obj_id:int):
        res = self.__exists_id_in_cache__(cache_key,obj_id)
        if res["status"]:
            return res["obj"]