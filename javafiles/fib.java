class fib{
    void printfib(int a,int b,int n){
        int c=a+b;
        System.Out.println(c);
        printfib(b,c,n-1);
    }
    public static void main (String args[]){
        int a=0,b=1;
        System.Out.println(a + " " + b);
        int n=7;
        printfib(a,b,n-2);
    }
}