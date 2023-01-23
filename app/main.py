"""
Rock Paper Scissors Using FastAPI
"""
from random import randrange
from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

# import pdb

VALID_HAND = ("rock", "paper", "scissors")
GAME_RULES = {
        ('paper', 'rock'): "win",
        ('paper', 'scissors'): "lose",
        ('paper', 'paper'): "lose",
        ('scissors', 'rock'): "lose",
        ('scissors', 'paper'): "win",
        ('scissors', 'scissors') : "tie",
        ('rock', 'paper'): "lose",
        ('rock', 'scissors'): "win",
        ('rock', 'rock'): "tie"
    }
SCORE = {"player": 0, "computer": 0}
GAMES = []
app = FastAPI()

class MyHand(BaseModel):
    """
    Represent the choice of the player during the game
    Args:
        BaseModel (Object): Create a new model by parsing and validating input data
    """
    myHand: str

@app.post("/play", status_code=200)
async def play(my_hand: MyHand, response: PlainTextResponse):
    """
    Method use to play against IA
    Args:
        my_hand (MyHand): Represent you weapon choice
        response (PlainTextResponse): media_type of the Post response

    Returns:
        Response object: Http response & code
    """
    my_hand_dict = my_hand.dict()
    ia_hand = {"iaHand": VALID_HAND[randrange(0, 3)]}
    if my_hand_dict["myHand"] in VALID_HAND:
        result = GAME_RULES[(my_hand_dict['myHand'], ia_hand['iaHand'])]
        message = f"You played {my_hand_dict['myHand']}, AI played {ia_hand['iaHand']}, you {result}"
        if result == "win":
            SCORE["player"] = SCORE["player"] + 1
            return PlainTextResponse(content=message, status_code=status.HTTP_201_CREATED)
        if result == "lose":
            SCORE["computer"] = SCORE["computer"] + 1
            return PlainTextResponse(content=message, status_code=status.HTTP_204_NO_CONTENT)
        return PlainTextResponse(status_code=status.HTTP_418_IM_A_TEAPOT)
    response.status_code = status.HTTP_400_BAD_REQUEST

@app.get("/results", status_code=200)
async def results():
    """
    Show the results of the games
    Returns:
        str : list of the object score
    """
    message = str(GAMES)
    return PlainTextResponse(content=message)

@app.get("/reset", status_code=200)
async def reset():
    """
    Reset the game and store the score
    """
    global SCORE
    GAMES.append(SCORE)
    SCORE = {"player": 0, "computer": 0}
