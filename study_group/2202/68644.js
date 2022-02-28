function solution(numbers) {
    var answer = [];
    for (let x = 0 ; x < numbers.length ; x++){
        for (let y = x+1 ; y < numbers.length; y++){
            answer.push(numbers[x]+numbers[y]);
        }
    }
    answer = [...new Set(answer)];
    return answer.sort((a,b) => a-b);
}