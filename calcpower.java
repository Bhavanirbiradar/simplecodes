public class calcpower {
    
    public static int calpower(int x,int n){
        if(n==0){
            return 1;
          
        }
        if(x==0){
            return 0;
        }
        int pow=calpower(x,n-1);
        int powern=x*pow;
        return powern;
       
    }
    
    public static void main (String args[]){
       int x=5,n=3;
       
       int res=calpower(x,n);
       System.out.println(res);
    }
}
    

