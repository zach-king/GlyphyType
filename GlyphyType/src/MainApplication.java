import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.io.*;


public class MainApplication {
	public static void main(String[] args) {
		System.out.println("Da fuq do you expect from me!?");
		System.out.println("Screw you, Blake.");
		
      JFrame window = new JFrame("Simple Paint");
      DrawingPanel content = new DrawingPanel();
      window.setContentPane(content);
      window.setSize(600,480);
      window.setLocation(100,100);
      window.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
      window.setVisible(true);
	}
	
	public static class DrawingPanel extends JPanel implements MouseListener, MouseMotionListener {
		
		// Select-able color constants
		private final static int BLACK = 0,
				RED = 1,
				GREEN = 2,
				BLUE = 3,
				WHITE = 4;
		
		// The currently selected color; uses the above color constants
		private int currentColor = BLACK;
		
		// Variables used while user is drawing freehand
		private int prevX, prevY; 				// The previous location of the mouse.
		private boolean isDragging; 			// True while the user is drawing.
		private Graphics graphicsForDrawing; 	// A graphics context for the panel
        										// that is used to draw the user's glyph.
		private int drawingWidth; 				// The width of the lines to be drawn.
		
		/**
		 * Constructor for DrawingPanel; sets the background 
		 * color to white, and starts listening for mouse events on itself.
		 */
		DrawingPanel() {
			setBackground(Color.WHITE);
			addMouseListener(this);
			addMouseMotionListener(this);
		}

		@Override
		public void mouseDragged(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseMoved(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseClicked(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseEntered(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseExited(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mousePressed(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseReleased(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}
		
	}

}
