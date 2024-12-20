import requests


class ChessDotComService:

    USER_AGENT = "MyApp/1.0"
    BASE_URL = "https://api.chess.com/pub"
    HEADERS = {"User-Agent": USER_AGENT}
        
    @staticmethod
    def get_player_stats(username):
        url = f"{ChessDotComService.BASE_URL}/player/{username}/stats"
        response = requests.get(url,headers=ChessDotComService.HEADERS)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_player_current_games(username):
        url = f"{ChessDotComService.BASE_URL}/player/{username}/games"
        response = requests.get(url,headers=ChessDotComService.HEADERS)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_player_game_by_id(username, game_id):
        url = f"{ChessDotComService.BASE_URL}/player/{username}/game/{game_id}"
        response = requests.get(url,headers=ChessDotComService.HEADERS)
        response.raise_for_status()
        return response.json()
    
    @staticmethod
    def get_player_archives_games(username,date) -> str:
        year = date.year
        month = date.month
        url = f"{ChessDotComService.BASE_URL}/player/{username}/games/{year}/{month}"
        response = requests.get(url, headers=ChessDotComService.HEADERS)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_user_pgns(username, date) -> str:
        url = f"{ChessDotComService.BASE_URL}/player/{username}/games/{date.year}/{date.month}/pgn"
        response = requests.get(url, headers=ChessDotComService.HEADERS)
        response.raise_for_status()
        return response.text
    
