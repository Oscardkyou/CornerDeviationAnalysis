import pandas as pd
import matplotlib.pyplot as plt
import os

class Plotter:
    def draw_plots(self, json_url):
        # Read JSON file as pandas dataframe
        df = pd.read_json(json_url)

        # Create 'plots' folder if not exists
        if not os.path.exists('plots'):
            os.makedirs('plots')

        # List to store paths to the plots
        plot_paths = []

        # Compare gt_corners with rb_corners
        fig, ax = plt.subplots()
        ax.plot(df['gt_corners'], label='Ground Truth Corners')
        ax.plot(df['rb_corners'], label='Model Corners', linestyle='dashed')
        plt.xlabel('Room')
        plt.ylabel('Number of Corners')
        plt.legend()
        plt.title('Ground Truth Corners vs Model Corners')
        plt.xticks(rotation=45)
        plot_path = 'plots/Gt_corners_vs_Rb_corners.png'
        plt.savefig(plot_path)
        plt.close(fig)
        plot_paths.append(plot_path)

        # Add more plots if needed

        return plot_paths

plotter = Plotter()
plotter.draw_plots('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')
