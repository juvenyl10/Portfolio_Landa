/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exer;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement; 
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import java.util.Scanner;


/**
 *
 * @author Juvenyl
 */
public class Exer {
    public static Connection myConn = null;
    public static PreparedStatement myPStmt = null;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        try {            
            Class.forName("com.mysql.jdbc.Driver"); 
            myConn = DriverManager.getConnection("jdbc:mysql://localhost:3306/exer","root", "");
            System.out.println("Connected");
        }
        catch (ClassNotFoundException | SQLException e) {
            System.out.println("Failed");
        }

        System.out.println("Enter name: ");
        String name = scan.nextLine();
        System.out.println("Enter age: ");
        int age = scan.nextInt();
        
        try{
            String sql = "INSERT INTO name (name, age) VALUES (?,?)";
            myPStmt = myConn.prepareStatement(sql);
            myPStmt.setString(1,name);
            myPStmt.setInt(2,age);
            myPStmt.executeUpdate();
            System.out.println("Data Added");
        }
        catch (SQLException e){
            System.out.println("error");
            
        }
    }
    
}
