package debugging;


public class debug {
	public static void main(String[] args) {
		System.out.println(calculateSquaredError(5, 3)); //
	}
	
	public static int calculateSquaredError(int value, int groundTruth) {
		int error = value - groundTruth;
		int squaredError = error ^ 2;
		return squaredError;
	}
}