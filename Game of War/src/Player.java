import java.util.*;

/**
 * Represents a WarGame-playing Player.
 * @author 
 *
 */
public class Player {
    public List<Card> unplayedPile;
    public List<Card> winningsPile;
    public List<Card> warPile;
    
    /**
     * Constructor.
     * Creates three lists to represent the player's unplayed pile,
     * winnings pile, and war pile.
     */
    public Player(){
    		List<Card> unplayedPile = new ArrayList<Card>();
    		List<Card> winningsPile = new ArrayList<Card>();
    		List<Card> warPile = new ArrayList<Card>();
    }
    
//    /**
//     * Adds card to the player's unplayed pile.
//     * @param card the card to add
//     */
//    public void addToUnplayedPile(Card card) {
//    		unplayedPile.add(card);
//    }
//    
//    /**
//     * Adds card to the player's winnings pile.
//     * @param card the card to add
//     */
//    public void addToWinningsPile(Card card) {
//    		winningsPile.add(card);
//    }
//    
//    /**
//     * Adds card to the player's war pile.
//     * @param card the card to add
//     */
//    public void addToWarPile(Card card) {
//    		warPile.add(card);
//    }
    
//    /**
//     * Removes and returns a card from the player's unplayed pile.
//     * @return Card the card 
//     */
//    public Card getCard(){
//    		return unplayedPile.remove(unplayedPile.size() - 1);
//    }
    
//    /**
//     * 
//     * @return 
//     */
//    public Boolean isDone() {
//    		if (unplayedPile.size() == 0) {
//    			return true;
//    		}
//    		else {
//    			return false;
//    		}
//    }
    
//    public int winningsCount() {
//    		return winningsPile.size();
//    }
}
