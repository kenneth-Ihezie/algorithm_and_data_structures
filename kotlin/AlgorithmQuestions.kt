import java.util.*
import kotlin.collections.ArrayList
import kotlin.math.log2

class AlgorithmQuestions {
    fun superReducedString(s: String): String {
         fun exit(s: String): Boolean{
             val flag = false
             val arrList = ArrayList<Boolean>()
             if(s.length - 2 == 0){
                 for (i in 0 until s.length - 1){
                     arrList.add(s[i] != s[i + 1])
                 }
             } else {
                 for (i in 0 until s.length - 2){
                     arrList.add(s[i] != s[i + 1])
                 }
             }
             return if (flag in arrList){
                 flag
             } else {
                 true
             }
         }
         if (exit(s)) {
             return if(s.isEmpty()){
                 "Empty String"
             } else {
                 s
             }
         }
         val size = s.length - 1
         var count = 0
         var newString = ""
         while (count < size){
             if (s[count] == s[count+1]){
                 newString = s.removeRange(IntRange(count, count + 1))
             }
             count++
         }
         return superReducedString(newString)
     }

    fun camelCase(s: String): Int {
        var count = 0
        for (i in s){
            if (i.isUpperCase()){
                count++
            }
        }
        return count + 1
    }

    fun minimumNumber(n: Int, password: String): Int {
        var out = 0
        var num = 0
        var low = 0
        var upper = 0
        var special = 0
        val arrList = ArrayList<Int>()
        if(n < 6) {
            out = 6 - n
        } else {
            val numbers = "0123456789"
            val lowerCase = "abcdefghijklmnopqrstuvwxyz"
            val upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            val specialCharacters = "!@#$%^&*()-+"

            for (i in password){
                if (i in numbers){
                    num++
                    continue
                } else if (i in lowerCase){
                    low++
                    continue
                } else if (i in upperCase) {
                    upper++
                    continue
                } else if (i in specialCharacters){
                    special++
                    continue
                }
            }
            arrList.add(num)
            arrList.add(low)
            arrList.add(upper)
            arrList.add(special)
            for (i in arrList){
                if (i == 0){
                    out++
                }
            }
        }
        return out
    }

    fun binarySearch(arr: ArrayList<Int>, x: Int): String{
        val mid = arr.size / 2
        println("Big o time complexity of this function is: " +
                "${log2((arr.size - 1).toFloat())}")
        if (x > arr[mid]){
            for (i in mid until arr.size - 1){
                if (i == x){
                    return "x is greater than mid: $i"
                }
            }
        } else {
            for (i in 0 until mid){
                if (i == x){
                    return "x is less than mid: $i"
                }
            }
        }
        return ""
    }

    fun graphAlogrithm(){

    }
}