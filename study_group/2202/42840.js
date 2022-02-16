function solution(answers) {
    const stu1 = [1,2,3,4,5]
    const stu2 = [2,1,2,3,2,4,2,5]
    const stu3 = [3,3,1,1,2,2,4,4,5,5]
    let score = [0,0,0]
    let result = []
    let max = 0
    for (let index=0; index<answers.length; index++){
        if (answers[index] == stu1[index%(stu1).length]){
            score[0]++;
        }
        if (answers[index] == stu2[index%(stu2).length]){
            score[1]++;
        }
        if (answers[index] == stu3[index%(stu3).length]){
            score[2]++;
        }
    }
    for (let x = 0; x<3; x++){
        if (max < score[x]){
            max = score[x]
        }
    }
    for (let x = 0; x<3; x++){
        if (max == score[x]){
            result.push(x+1)
        }
    }
    return result
}

// let test_case = [1,2,3,4,5];
let test_case = [1,3,2,4,2];
// let test_case = [3, 3, 2, 1, 5];
console.log(solution(test_case));