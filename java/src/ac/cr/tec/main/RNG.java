package ac.cr.tec.main;

import java.util.Random;

public class RNG {

    public double generateRandom(){
        Random random = new Random();
        return random.nextDouble();
    }

}
