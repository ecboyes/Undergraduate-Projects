/**
 * the model
 * Represents a the game of War.
 * @author 
 *
 */
public class WarGame{
	public Player player1;
	public Player player2;
	public Deck deck;
	
    /**
     * Constructor. Sets up a game of War.
     * Instantiates a deck and shuffles it. Creates 2 players.
     * Distributes deck between the players randomly.
     */
	public WarGame(){
		Player player1 = new Player();
		Player player2 = new Player();
		Deck deck = new Deck();
		deck.shuffle();
		for (int i = 0; i <= 25; i++) {
			player1.unplayedPile.add(deck.deal());
		}
		for (int i = 0; i <= 25; i++) {
			player2.unplayedPile.add(deck.deal());
		}
	}
	
	/**
	 * Executes a move in the game of War.
	 */
	public void move(){
		player1.warPile.add(player1.unplayedPile.remove(player1.unplayedPile.size() - 1));
		player2.warPile.add(player2.unplayedPile.remove(player2.unplayedPile.size() - 1));
		if (player1.warPile.get(player1.warPile.size()).compareTo(player2.warPile.get(player2.warPile.size())) > 0){
			player1.winningsPile.addAll(player1.warPile);
			player1.winningsPile.addAll(player2.warPile);
		}
		if (player1.warPile.get(player1.warPile.size()).compareTo(player2.warPile.get(player2.warPile.size())) < 0){
			player2.winningsPile.addAll(player1.warPile);
			player2.winningsPile.addAll(player2.warPile);
		}	
		
//	public void newGame(){
//		WarGame();
////		player1.unplayedPile.clear();
////		player1.winningsPile.clear();
////		player1.warPile.clear();
////		player2.unplayedPile.clear();
////		player2.winningsPile.clear();
////		player2.warPile.clear();
////		deck.
//	}
		
	}
}
