
public class Vector {
	private int size;
	private double arr[];
	
	public Vector(double[] arr, int size) {
		this.arr = arr;
		this.size = size;
	}
	
	public int getSize() {
		return size;
	}
	
	public double getIndex(int index) {
		return arr[index];
	}
	
	public void setIndex(int index, double set) {
		arr[index] = set;
	}
	
	public int getLenght() {
		return arr.length;
	}
	
	public void bubbleSort() {
		for(int i = arr.length-1 ; i > 0 ; i--){
	        for(int j = 0 ; j < i ; j++){
	            if( arr[j] > arr[j+1] ){
	                double tmp = arr[j];
	                arr[j] = arr[j+1];
	                arr[j+1] = tmp;
	            }
	        }
	    }
	}
	
	public double minNumber() {
		double min = Double.MAX_VALUE;
		for(int i = 0; i < arr.length; i++)
		{
			if(min > arr[i])
			{
				min = arr[i];
			}
		}
		return min;
	}
	
	public double maxNumber() {
		double max = Double.MIN_VALUE;
		for(int i = 0; i < arr.length; i++)
		{
			if(max < arr[i])
			{
				max = arr[i];
			}
		}
		return max;
	}
	
	public double evklid() {
		double result = 0;
		for(int i = 0; i < arr.length; i++)
		{
			result += arr[i] * arr[i];
		}
		return Math.sqrt(result);
	}
	
	public void multi(double b) {
		for(int i = 0; i < arr.length; i++)
		{
			arr[i] *= b;
		}
	}
	public void sumVectors(Vector vector) {
		if(a == vector.getSize())
		{
			for(int i = 0; i < arr.length; i++)
			{
				arr[i] += vector.getIndex(i);
			}
		}
		
		else
			System.out.println("!");
	}
	
	public double multiVectors(Vector vector) {
		double result = 0;
		for(int i = 0; i < arr.length; i++)
		{
			result += arr[i] * vector.getIndex(i);
		}
		return result;
	}
}
