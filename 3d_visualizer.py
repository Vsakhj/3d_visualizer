import matplotlib.pyplot as plt
import numpy as np
import os

# --- Configuration ---
OUTPUT_DIR = '3d_visualizations'
OUTPUT_FILENAME = '3d_scatter_cube.png'

# --- Functions ---
def create_output_directory(directory_name):
    """Creates a directory if it doesn't already exist."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Created output directory: {directory_name}")
    else:
        print(f"Output directory '{directory_name}' already exists.")

def generate_3d_cube_points(side_length=1.0):
    """
    Generates the 8 vertices of a simple 3D cube for visualization.
    Returns three NumPy arrays for x, y, and z coordinates.
    """
    half_side = side_length / 2.0
    
    # Define the 8 vertices of a cube
    x = np.array([-half_side, half_side, -half_side, half_side,
                  -half_side, half_side, -half_side, half_side])
    y = np.array([-half_side, -half_side, half_side, half_side,
                  -half_side, -half_side, half_side, half_side])
    z = np.array([-half_side, -half_side, -half_side, -half_side,
                  half_side, half_side, half_side, half_side])
    
    print("Generated 8 vertices for a 3D cube.")
    return x, y, z

def visualize_3d_scatter(x_coords, y_coords, z_coords, output_dir, filename):
    """
    Creates a 3D scatter plot from the given coordinates and saves it as an image.
    """
    print("\nCreating 3D scatter plot...")
    
    # Create a new figure and a 3D Axes object
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the scatter points
    ax.scatter(x_coords, y_coords, z_coords, c='blue', marker='o', s=100)
    
    # Set labels for the axes
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Scatter Plot of Cube Vertices')
    
    # Optional: Adjust view angle for better visualization
    ax.view_init(elev=20, azim=45) # elevation, azimuth
    
    # Save the plot to a file
    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path)
    print(f"3D scatter plot saved to: {output_path}")
    
    # Display the plot
    print("Displaying 3D plot. Close window to continue...")
    plt.show()
    print("3D plot window closed.")

# --- Main execution block ---
if __name__ == "__main__":
    create_output_directory(OUTPUT_DIR)
    
    # Generate coordinates for a simple cube
    cube_x, cube_y, cube_z = generate_3d_cube_points()
    
    # Visualize the 3D points
    visualize_3d_scatter(cube_x, cube_y, cube_z, OUTPUT_DIR, OUTPUT_FILENAME)
    
    print("\n3D visualization work sample complete. Check the '3d_visualizations' directory for output.")