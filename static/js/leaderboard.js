class Player {
	constructor(name,points)
	{
		this.name = name;
		this.points = points;
	}
}
function getData()
{

    function loadDoc()
    {
        var arr=[];
        var xttp;
        xttp = new XMLHttpRequest();
        xttp.onreadystatechange= function() {
            if(this.readyState ==  4 && this.status==200)
            {
                arr.push({name:this.responseText.name,points:this.responseText.points});
            }
        };
        xttp.open("GET","ajax_info.txt",true);
        xttp.send();
        return arr;
}

};

var data = getData();
let scores = [
    {name: "Player 1", score: 300},
    {name: "Player 2", score: 370},
    {name: "Player 3", score: 500},
    {name: "Player 4", score: 430},
    {name: "Player 5", score: 340},{name: "Player 5", score: 340},{name: "Player 5", score: 340},{name: "Player 5", score: 340},{name: "Player 5", score: 340},
];
scores.sort((a,b) =>
    {return b.score - a.score;
    });
function updateLeaderboardView() {
    let leaderboard = document.getElementById("leaderboard");
    leaderboard.innerHTML = "";

    let elements = []; // we'll need created elements to update colors later on
    // create elements for each player
    let head = document.createElement("h2");
    head.innerText = "LeaderBoard";
    head.classList.add("heading");
    leaderboard.appendChild(head);
    for(let i=0; i<scores.length; i++) {
        let name = document.createElement("div");
        let num = document.createElement("div");
        let score = document.createElement("div");
        name.classList.add("name");
        score.classList.add("count");
        num.classList.add("rank");
        if(i+1==1)
            num.innerText = i+1+'ST';
        else if(i+1==2)
            num.innerText = i+1+'ND';
        else if(i+1==3)
            num.innerText = i+1+'RD';
        else
            num.innerText = i+1;
        name.innerText = scores[i].name;
        score.innerText = scores[i].score;
        let scoreRow = document.createElement("div");
        scoreRow.classList.add("row");
        scoreRow.appendChild(num);
        scoreRow.appendChild(name);
        scoreRow.appendChild(score);
        leaderboard.appendChild(scoreRow);
        elements.push(scoreRow);

    }
}
updateLeaderboardView();

