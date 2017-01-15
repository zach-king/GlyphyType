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
				CYAN = 4,
				MAGENTA = 5,
				YELLOW = 6;
		
		// The currently selected color; uses the above color constants
		private int currentColor = BLACK;
		
		// The thickness of the curves
		private int thickness = 1;
		
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
		
		/**
		 * Draw the contents of the panel. Since no information is
		 * saved about what the user has drawn, the user's drawing
		 * is erased whenever this routine is called.
		 */
		public void paintComponent(Graphics g) {
			super.paintComponent(g); // Fill with background color (white)
			
			int width = getWidth(); // Width of the panel
			int height = getHeight(); // Height of the panel
			
			int colorSpacing = (height - 56) / 7;
			
			/* Draw a 3-pixel wide gray border around the applet. 
			 * This has to be drawn with 3 rectangles of different size.
			 */
			g.setColor(Color.GRAY);
			g.drawRect(0, 0, width-1, height-1);
			g.drawRect(1, 1, width-3, height-3);
			g.drawRect(2, 2, width-5, height-5);
			
			/* Draw a 56-pixel wide gray rectangle along the right edge of the app.
			 * The color palette and Clear button will be drawn on top of this.
			 * (This covers some of the same area as the border I just drew. */
			g.fillRect(width - 56, 0, 56, height);
			
			/* Draw the "Clear button" as a 50-by-50 white recangle in the lower
			 * right corner of the app, allowing for a 3-pixel border. */
			g.setColor(Color.WHITE);
			g.fillRect(width - 53, height - 53, 50, 50);
			g.setColor(Color.BLACK);
			g.drawRect(width-53, height-53, 49, 49);
			g.drawString("CLEAR", width-48, height-23);
			
			/* Draw the seven color rectangles */
			g.setColor(Color.BLACK);
			g.fillRect(width - 53, 3 + 0*colorSpacing, 50, colorSpacing - 3);
			g.setColor(Color.RED);
			g.fillRect(width - 53, 3 + 1*colorSpacing, 50, colorSpacing - 3);
			g.setColor(Color.GREEN);
			g.fillRect(width - 53, 3 + 2*colorSpacing, 50, colorSpacing - 3);
			g.setColor(Color.BLUE);
			g.fillRect(width - 53, 3 + 3*colorSpacing, 50, colorSpacing - 3);
			g.setColor(Color.CYAN);
			g.fillRect(width - 53, 3 + 4*colorSpacing, 50, colorSpacing - 3);
			g.setColor(Color.MAGENTA);
			g.fillRect(width - 53, 3 + 5*colorSpacing, 50, colorSpacing - 3);
			g.setColor(Color.YELLOW);
			g.fillRect(width - 53, 3 + 6*colorSpacing, 50, colorSpacing - 3);
			
			/* Draw a 2-pixel white border around the color rectanlge
			 * of the current drawing color. */
			g.setColor(Color.WHITE);
			g.drawRect(width - 55, 1 + currentColor*colorSpacing, 53, colorSpacing);
			g.drawRect(width - 54, 2 + currentColor*colorSpacing, 51, colorSpacing - 2);
		} // end paintComponent()
		
		/**
		 * Change the drawing color after the user has clicked the 
		 * mouse on the color palette at a point with y-coordinate y.
		 * (Note that I can't just call repaint and redraw the whole
		 * panel, since that would erase the user's drawing.
		 */
		private void changeColor(int y) {
	         
	         int width = getWidth();           // Width of applet.
	         int height = getHeight();         // Height of applet.
	         int colorSpacing = (height - 56) / 7;  // Space for one color rectangle.
	         int newColor = y / colorSpacing;       // Which color number was clicked?
	         
	         if (newColor < 0 || newColor > 6)      // Make sure the color number is valid.
	            return;
	         
	         /* Remove the hilite from the current color, by drawing over it in gray.
	          Then change the current drawing color and draw a hilite around the
	          new drawing color.  */
	         
	         Graphics g = getGraphics();
	         g.setColor(Color.GRAY);
	         g.drawRect(width-55, 1 + currentColor*colorSpacing, 53, colorSpacing);
	         g.drawRect(width-54, 2 + currentColor*colorSpacing, 51, colorSpacing-2);
	         currentColor = newColor;
	         g.setColor(Color.WHITE);
	         g.drawRect(width-55, 1 + currentColor*colorSpacing, 53, colorSpacing);
	         g.drawRect(width-54, 2 + currentColor*colorSpacing, 51, colorSpacing-2);
	         g.dispose();
	         
	      } // end changeColor()
		
		/**
		 * This routine is called in mousePressed when the user clicks on the drawing area.
		 * it sets up the graphics context, graphicsForDrawing, to be used to draw the user's
		 * sketch in the current color.
		 */
		private void setUpDrawingGraphics() {
			graphicsForDrawing = getGraphics();
			
			switch (currentColor) {
			case BLACK:
				graphicsForDrawing.setColor(Color.BLACK);
				break;
			case RED:
				graphicsForDrawing.setColor(Color.RED);
				break;
			case GREEN:
				graphicsForDrawing.setColor(Color.GREEN);
				break;
			case BLUE:
				graphicsForDrawing.setColor(Color.BLUE);
				break;
			case CYAN:
				graphicsForDrawing.setColor(Color.CYAN);
				break;
			case MAGENTA:
				graphicsForDrawing.setColor(Color.MAGENTA);
				break;
			case YELLOW:
				graphicsForDrawing.setColor(Color.YELLOW);
				break;
			}
		} // end setUpDrawingGraphics()

		/**
		 * Called whenever the user moves the mouse while a mouse button is held down.
		 * If the user is drawing, draw a line segment from the previous mouse location 
		 * to the current mouse location, and set up prevX and prevY for the next call.
		 * Note that in case the user drags outside of the drawing area, the values of 
		 * x and y are "clamped" to lie within this area. This avoids drawing on the color 
		 * palette or clear button.
		 */
		@Override
		public void mouseDragged(MouseEvent evt) {
			if (!isDragging) 
				return; // Nothing to do because user isn't drawing
			
			int x = evt.getX(); // x-coord. of mouse
			int y = evt.getY(); // y-coord. of mouse
			
			if (x < 3)
				x = 3; // clamp x to start at 3
			if (x > getWidth() - 57)
				x = getWidth() - 57; // Clamp x to max at width - 57
			
			if (y < 3)
				y = 3; // clamp y to start at 3
			if (y > getHeight() - 4)
				y = getHeight() - 4;
			
			for (int i = 1; i <= thickness; i++)
				graphicsForDrawing.drawLine(i+prevX, i+prevY, i+x, i+y); // Draw the line
			
			prevX = x; // Get ready for next call
			prevY = y;
		} // end mouseDragged()

		/**
		 * This is called when ther user presses the mosue anywhere in the app.
		 * There are three possible responses, depending on where the user clicked:
		 * Change the current color, clear the drawing, or start drawing a curve.
		 * (Or do nothing if user clicks on border.)
		 */
		@Override
		public void mousePressed(MouseEvent e) {
			int x = e.getX(); // x-coordinate where user clicked
			int y = e.getY(); // y-coordinate where user clicked
			
			int width = getWidth(); 	// Width of the panel
			int height = getHeight(); 	// Height of the panel
			
			if (isDragging) // Ignore mouse presses that occur
				return; 	// when user is already drawing a curve.
							// (This can happen if the uesr presses
							// two mouse buttons at the same time.)
			
			if (x > width - 53) {
				// User clicked to the right of the drawing area.
				// This click is either on the clear button or 
				// on the color palette
				if (y > height - 53)
					repaint(); 		// Clicked on "CLEAR" button
				else
					changeColor(y); // Clicked on the color palette
			}
			else if (x > 3 && x < width - 56 && y > 3 && y < height - 3) {
				// The user has clicked on the white drawing area.
				// Start drawing a curve from the point (x, y).
				prevX = x;
				prevY = y;
				isDragging = true;
				setUpDrawingGraphics();
			}
		} // end mousePressed()

		/**
		 * Called whenever the user releases the mouse button. If the user was drawing
		 * a curve, the curve is done, so we should set drawing to false and get rid of 
		 * the graphics context that we created to use during the drawing.
		 */
		@Override
		public void mouseReleased(MouseEvent e) {
			if (!isDragging)
				return; // Nothing to do because user isn't drawing
			
			isDragging = false;
			graphicsForDrawing.dispose();
			graphicsForDrawing = null;
		}
		
		@Override
		public void mouseMoved(MouseEvent arg0) { }

		@Override
		public void mouseClicked(MouseEvent e) { }

		@Override
		public void mouseEntered(MouseEvent e) { }

		@Override
		public void mouseExited(MouseEvent e) { }
		
	}

}
