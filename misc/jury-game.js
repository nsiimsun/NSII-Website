let post = {
    "pos": 0,
    "score": 0,
    "count": 0,
    "tot": 18,
    0: ["Some text", 0],
    1: ["The last election was rigged", 0],
    2: ["Masks save lives", 1],
    3: ["Pfizer is injecting microchips", 0],
    4: ["I hate you", 1],
    5: ["Zelda is my favorite game", 1],
    6: ["Wuhan engineered the Wuhan Virus", 0],
    7: ["Donald Trump is a fascist", 0],
    8: ["Barack Obama was born in Libya", 0],
    9: ["Orange is my favorite color", 1],
    10: ["Pierre Trudeau was the Canadian PM during the '70s", 1],
    11: ["The United States President is a lizard", 0],
    12: ["The gay-related immune defficiency only kills gay people", 0],
    13: ["Canada is mourning over 215 unmarked graves in Kamloops", 1],
    14: ["Canada Day is July 4th", 0],
    15: ["Joe Biden has dementia", 0],
    16: ["Donald Trump has dementia", 0],
    17: ["Justin Trudeau is reopening the US-Canada border", 1],
    18: ["Black police officers often kill innocent people", 0]
};

let score = 0; 
let count = 0;
function score_post(post, mod){
    post["count"]++
    if(post["count"] == 1) {
        new_post(post);
        return;
    }
    if (post[post["pos"]][1] == mod) {
	    post["score"]++;
    }
    new_post(post);
}

function new_post(post){
    if (post["pos"] < post["tot"]) {
        post["pos"]++;
        document.getElementById("post_container").innerHTML = post[post["pos"]][0];
    }
    else
        game_over(post);
}

function game_over(post){
    let score = Math.round(post["score"] * 100.0 / (post["count"] - 1));
    document.getElementById("post_container").innerHTML = "You got a score of: " + score + "%";
    document.getElementById("yesbtn").style.visibility = "hidden";
    document.getElementById("nobtn").style.visibility = "hidden";
}
