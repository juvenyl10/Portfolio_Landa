/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.mastertheorem;

/**
 *
 * @author Juvenyl
 */
import java.util.Scanner;

public class Mastertheorem {

    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        while(true){
            System.out.print("Enter value for a: ");
            int a = scan.nextInt();
            System.out.print("Enter value for b: ");
            int b = scan.nextInt();
            System.out.print("Enter f(n): ");
            int fn = scan.nextInt();
//            scan.nextLine(); 
//            String fn = scan.nextLine();

            double log = Math.log(a) / Math.log(b);
            System.out.println("\nn^logb^a:  " + String.format("%.2f", log));
            
            if (log > fn){
                System.out.print("Case 1");
            }
            else if (log == fn){
                System.out.print("Case 2");
            }
            else if (log < fn){
                System.out.print("Case 3");
            }
            System.out.print("\n");
        }
    }
    
}
//
//import java.util.Scanner;
//
//public class Master_Theorem {
//
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//
//        System.out.print("Enter the value of a: ");
//        int a = scanner.nextInt();
//
//        System.out.print("Enter the value of b: ");
//        int b = scanner.nextInt();
//
//        System.out.print("Enter the exponent k of f(n) = O(n^k): ");
//        int k = scanner.nextInt();
//
//        // Calculate log_b(a)
//        double log_b_a = Math.log(a) / Math.log(b);
//
//        // Determine the case of the Master Theorem
//        System.out.println("Log_b(a) = " + log_b_a);
//
//        if (k < log_b_a) {
//            System.out.printf("Case 1: T(n) = Θ(n^%.2f)\n", log_b_a);
//        } else if (k == log_b_a) {
//            System.out.printf("Case 2: T(n) = Θ(n^%.2f * log^k(n))\n", log_b_a);
//        } else {
//            System.out.println("Case 3: T(n) = Θ(n^" + k + ")");
//        }
//
//        scanner.close();
//  }
//}
