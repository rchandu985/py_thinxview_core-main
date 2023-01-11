// Your First Program

class HelloWorld {
    
    
    public static void main(String[] args) {
        int a []={1,100,2,3,10,4};
        int y=0;
        for(int i=0; i<a.length; i++){
            if(a[i]>y){
                y=a[i];
            }
            
        }

        System.out.println(y);    }       
}