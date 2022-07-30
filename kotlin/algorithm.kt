/*
fun main(){
    println("hello")
    for (i in arrayOf(1,2,3,5)){
        println(i)
    }
    val c = {a: Int, b: Int ->
        a + b
    }
    println(c(2, 2))

    val stringArr = arrayOf("b", "m", "a")
    stringArr.sort()
    for(i in stringArr){
        println(i)
    }
}
*/


fun main() {
    val algorithmQuestions = AlgorithmQuestions()
    /*val input = "aa"
    var output = algorithmQuestions.superReducedString(input)*/
   /* val input = "oneTwoAgoTheCatGozieOneTey"
    val output = algorithmQuestions.camelCase(input)*/
   /* val input = "aaabbb"
    val output = algorithmQuestions.minimumNumber(6, input)*/
    val input = ArrayList<Int>()
    for (i in 0..10){
        input.add(i)
    }
    val output = algorithmQuestions.binarySearch(input, 3)
    println(output)
}
