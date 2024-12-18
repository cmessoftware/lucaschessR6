import datetime
import requests


class ChessDotComService:

    USER_AGENT = "MyApp/1.0"

    def __init__(self):
        self.base_url = "https://api.chess.com/pub"
        self.headers = {"User-Agent": self.USER_AGENT}  # Use a descriptive value
        
    def get_player_stats(self, username):
        url = f"{self.base_url}/player/{username}/stats"
        response = requests.get(url,headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_player_current_games(self, username):
        url = f"{self.base_url}/player/{username}/games"
        response = requests.get(url,headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_player_game_by_id(self, username, game_id):
        url = f"{self.base_url}/player/{username}/game/{game_id}"
        response = requests.get(url,headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_player_archives_games(self, username,date):
        year = date.year
        month = date.month
        url = f"{self.base_url}/player/{username}/games/{year}/{month}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_user_pgns(self, username, date):
        url = f"{self.base_url}/player/{username}/games/{date.year}/{date.month}/pgn"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.text
    
# if __name__ == "__main__":
#     service = ChessDotComService()
#     username = "cmess4401"
    
#     try:
#         stats = service.get_player_stats(username)
#         print("Player Stats:", stats)
#         print("*************************************************************************************")
#         games = service.get_player_current_games(username)
#         print("Player Currents Games:", games)
#         print("*************************************************************************************")
#         # Example game_id, replace with a valid one if needed
#         # game_id = "127950583979"
#         # game = service.get_player_game_by_id(username, game_id)
#         # print("Player Game by ID:", game)
#         # print("*************************************************************************************")
#         png = service.get_player_archives_games(username, date = datetime.date(2024, 12, 1) )
#         print("Player Archives Games:", png)
        
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
        
        
        
