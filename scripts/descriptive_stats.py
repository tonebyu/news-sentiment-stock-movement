import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_descriptive_stats(df, column_name='headline'):
    """
    Compute and display descriptive statistics for the specified column in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    column_name (str): The name of the column to analyze. Default is 'headline'.

    Returns:
    dict: A dictionary containing descriptive statistics.
    """
    # Ensure the column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Calculate lengths of the specified column
    lengths = df[column_name].astype(str).apply(len)

    # Compute descriptive statistics
    stats = {
        'min': lengths.min(),
        'max': lengths.max(),
        'mean': lengths.mean(),
        'median': lengths.median(),
        'std': lengths.std()
    }

    # Display statistics
    print("Descriptive Statistics for column '{}':".format(column_name))
    for stat, value in stats.items():
        print(f"{stat.capitalize()}: {value}")

    # Plot histogram of lengths
    plt.figure(figsize=(10, 6))
    plt.hist(lengths, bins=50, color='blue', alpha=0.7)
    plt.title(f'Distribution of {column_name} Lengths')
    plt.xlabel('Length')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    return stats
def compute_publisher_article_counts(df, column_name='publisher'):
    """
    Compute and display the number of articles per publisher.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    column_name (str): The name of the column containing publisher names. Default is 'publisher'.

    Returns:
    pd.Series: A Series containing the counts of articles per publisher.
    """
    # Ensure the column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Compute article counts per publisher
    publisher_counts = df[column_name].value_counts()

    # Display counts
    print("Number of Articles per Publisher:")
    print(publisher_counts)

    # Plot bar chart of publisher article counts fro top 10 publishers
    top_publishers = publisher_counts.head(10)
    plt.figure(figsize=(12, 8))
    top_publishers.plot(kind='bar', color='green', alpha=0.7)
    plt.title('Top 10 Publishers by Number of Articles')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.75)
    plt.show()
    return publisher_counts

def analyze_publication_trends(df, date_column='date'):
    """
    Analyze publication trends over time based on the specified date column.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    date_column (str): The name of the column containing publication dates. Default is 'date'.

    Returns:
    pd.Series: A Series containing the counts of articles per date.
    """
    # Ensure the column exists
    if date_column not in df.columns:
        raise ValueError(f"Column '{date_column}' does not exist in the DataFrame.")

    # Convert to datetime if not already
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

    # Drop rows with invalid dates
    df = df.dropna(subset=[date_column])

    # Compute article counts per date
    date_counts = df[date_column].dt.date.value_counts().sort_index()

    # Display counts
    print("Number of Articles Published Over Time:")
    print(date_counts)

    # Plot time series of article counts
    plt.figure(figsize=(14, 7))
    date_counts.plot(kind='line', marker='o', color='orange', alpha=0.7)
    plt.title('Publication Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    return date_counts


