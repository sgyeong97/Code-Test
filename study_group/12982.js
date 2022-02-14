//프로그래머스 예산 문제

function solution(d, budget) {
    var answer = 0;
    for (let x in d.sort((a,b)=>a-b)){
        let temp = (budget-d[x]);
        if(temp >= 0){
            budget = temp;
            answer++;
        }
    }
    return answer;
}