import logging
from pathlib import Path
import math
from src.common_library import helper_functions as hf

#
# https://pynative.com/python-math-statistics-exercises/
# Exercises 21 through 30
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)




#########################################################################################
def exercise_21_quartiles_testing():
    """
    Exercise 21: Quartiles with statistics.quantiles()
    Problem Statement:
        Write a Python program that generates a dataset of 20 integers,
        uses statistics.quantiles() to compute Q1, Q2, and Q3, then
        uses these values to calculate the interquartile range (IQR)
        and identify any outliers using the IQR fence method.
    Purpose:
        Quartiles and the IQR are among the most robust tools in
        descriptive statistics. Unlike standard deviation, they are not
        sensitive to extreme outliers and are the basis of the box-and-whisker
        plot. The IQR fence method (Q1 – 1.5×IQR, Q3 + 1.5×IQR) is the
        standard algorithm used by statistical software to flag outliers
        in exploratory data analysis.
    Given Input:
        data = [4, 7, 13, 2, 19, 25, 8, 14, 3, 31, 11, 6, 17, 22, 9, 5, 28, 16, 10, 100]
        (20 integers including one obvious outlier)
    Expected Output:
        Q1, Q2, Q3, IQR, fence boundaries, and the list of
        values flagged as outliers by the IQR method.
    """
    logger.info(f"Exercise 21: Quartiles with statistics.quantiles()")
    pass



#########################################################################################
def exercise_22_harmonic_mean_testing():
    """
    Exercise 22: Harmonic Mean of Internet Speeds
    Problem Statement:
        Write a Python program that computes the harmonic mean
        of a list of internet speeds using statistics.harmonic_mean(),
        then compares it to the arithmetic mean to show why the
        harmonic mean is the correct average for rate-based
        measurements.
    Purpose:
        The harmonic mean is the correct average to use when
        combining rates, speeds, or ratios measured over equal
        distances or time slots. Using the arithmetic mean for
        speeds systematically overestimates the true average,
        leads to incorrect capacity planning, network benchmarking,
        and performance reporting. This exercise builds the
        intuition to recognize when each type of mean is appropriate.
    Given Input:
        speeds = [10, 20, 40, 80] (internet speeds in Mbps)
    Expected Output:
        Harmonic mean: 22.86 Mbps and Arithmetic mean: 37.50 Mbps
    """
    logger.info(f"Exercise 22: Harmonic Mean of Internet Speeds")
    pass



#########################################################################################
def exercise_23_geometric_mean_for_compound_growth():
    """
    Exercise 23: Geometric Mean for Compound Growth Rate
    Problem Statement:
        Write a Python program that uses statistics.geometric_mean()
        to calculate the average compound annual growth rate (CAGR)
        from five years of annual returns, then verifies the result
        by compounding the geometric mean over the same period.
    Purpose:
        The geometric mean is the correct average for quantities
        that multiply over time – investment returns, population
        growth rates, inflation rates, and biological reproduction
        factors. Using the arithmetic mean for such data overestimates
        the true long-term growth and leads to misleading projections.
        This is one of the most practically important distinctions in
        financial and scientific data analysis.
    Given Input:
        Annual growth factors for 5 years:
        growth_factors = [1.08, 0.95, 1.12, 1.06, 0.98]
        (representing +8%, -5%, +12%, +6%, -2%)
    Expected Output:
        Geometric mean (CAGR): 1.0369 meaning approximately 3.69% average annual growth.
    """
    logger.info(f"Exercise 23: Geometric Mean for Compound Growth Rate")
    pass



#########################################################################################
def exercise_24_covariance_testing():
    """
    Exercise 24: Covariance Between Study Hours and Test Scores
    Problem Statement:
        Write a Python program that uses statistics.covariance() to
        measure the linear relationship between hours studied and
        test scores, then interprets the sign and magnitude of
        the result.
    Purpose:
        Covariance is the foundational measure of how two variables
        move together. It is the building block of correlation,
        regression, and portfolio theory in finance. Understanding
        its sign (direction of relationship) and its scale-dependence
        (why raw covariance cannot be compared across different datasets)
        motivates the need for the normalized correlation coefficient
        introduced in the next exercise.
    Given Input:
        hours = [2, 4, 6, 8, 5, 7, 3, 9, 1, 6] and
        scores = [55, 70, 80, 92, 74, 85, 60, 95, 45, 78]
    Expected Output:
        A positive covariance value confirming that more
        study hours are associated with higher scores.
    """
    logger.info(f"Exercise 24: Covariance Between Study Hours and Test Scores")
    pass



#########################################################################################
def exercise_25_pearson_correlation_coefficient():
    """
    Exercise 25: Pearson Correlation Coefficient
    Problem Statement:
        Write a Python program that uses statistics.correlation()
        to compute the Pearson correlation coefficient between
        hours studied and test scores, interprets the strength
        and direction of the relationship, and verifies that it
        equals the covariance divided by the product of the two
        standard deviations.
    Purpose:
        The Pearson correlation coefficient is the most widely
        used measure of linear association in science, engineering,
        finance, and machine learning. Unlike covariance, its
        value is always between -1 and +1, making it directly
        comparable across datasets regardless of units.
        Understanding it deeply is a prerequisite for linear
        regression, feature selection, and multicollinearity
        analysis.
    Given Input:
        hours = [2, 4, 6, 8, 5, 7, 3, 9, 1, 6] and
        scores = [55, 70, 80, 92, 74, 85, 60, 95, 45, 78]
    Expected Output:
        Pearson r: 0.9934 indicating a
        very strong positive linear relationship.
    """
    logger.info(f"Exercise 25: Pearson Correlation Coefficient")
    pass



#########################################################################################
def exercise_26_probability_with_normal_distribution():
    """
    Exercise 26: Probability with NormalDist
    Problem Statement:
        Write a Python program that creates a statistics.NormalDist
        object with mean 70 and standard deviation 10, then calculates
        the probability of a student scoring above 85, below 60, and
        between 65 and 80.
    Purpose:
        NormalDist makes working with the normal (Gaussian)
        distribution straightforward without requiring external
        libraries like SciPy. It is used in grading, quality control
        (Six Sigma), A/B testing, risk modelling, and any domain
        where measurements cluster around a mean. This exercise
        introduces the CDF (cumulative distribution function),
        which answers the question “what fraction of values fall
        below this threshold?”
    Given Input:
        mu = 70, sigma = 10
    Expected Output:
        Probability of scoring above 85, below 60, and
        between 65 and 80, each expressed as a percentage.
    """
    logger.info(f"Exercise 26: Probability with NormalDist")
    pass



#########################################################################################
def exercise_27_distribution_overlap():
    """
    Exercise 27: Distribution Overlap Between Two Models
    Problem Statement:
        Write a Python program that uses NormalDist.overlap() to compute
        how much two normal distributions representing the error rates
        of two machine learning models overlap, then interprets what
        the overlap coefficient means for model comparison.
    Purpose:
        Overlap between distributions is a practical measure of how
        distinguishable two groups are – used in medical diagnostic
        accuracy (sensitivity vs specificity), A/B test analysis (are
        the two variants really different?), and model evaluation
        (do two models perform differently or are their results
        statistically indistinguishable?). NormalDist.overlap()
        computes this in one call without numerical integration.
    Given Input:
        Model A error rate: NormalDist(mu=0.15, sigma=0.03).
        Model B error rate: NormalDist(mu=0.22, sigma=0.04).
    Expected Output:
        An overlap coefficient between 0 and 1, with 1 meaning identical
        distributions and 0 meaning completely separate distributions.
    """
    logger.info(f"Exercise 27: Distribution Overlap Between Two Models")
    pass



#########################################################################################
def exercise_28_grading_curve_with_normal_distribution():
    """
    Exercise 28: Grading Curve with NormalDist.from_samples()
    Problem Statement:
        Write a Python program that uses NormalDist.from_samples() to
        fit a normal distribution to raw exam scores, then rescales all
        scores so that the distribution mean becomes 75, preserving the
        relative spread of the original grades.
    Purpose:
        Grade curving is a direct application of distribution shifting
        – adjusting all scores by a constant so the class mean hits a
        target without changing the relative ranking or spread.
        NormalDist.from_samples() provides a clean interface for fitting
        a distribution to observed data, and the resulting object’s
        parameters drive the rescaling logic.
    Given Input:
        raw_scores = [52, 61, 47, 73, 68, 55, 80, 44, 66, 71, 58, 49, 76, 63, 57]
    Expected Output:
        Original mean, target mean of 75, the shift applied,
        and the full list of curved scores.
    """
    logger.info(f"Exercise 28: Grading Curve with NormalDist.from_samples()")
    pass



#########################################################################################
def exercise_29_linear_regression_testing():
    """
    Exercise 29: Linear Regression to Predict Scores
    Problem Statement: Write a Python program that uses statistics.linear_regression()
        to fit a line to hours-studied and test-score data, then uses the resulting
        slope and intercept to predict the score for a student who studies 8 hours.
    Purpose: Linear regression is the most widely used predictive modelling
        technique in statistics and data science. statistics.linear_regression()
        was added in Python 3.10 as a lightweight built-in implementation for
        simple (single-variable) regression, removing the need for NumPy or
        scikit-learn for straightforward prediction tasks. Understanding slope
        and intercept lays the groundwork for all more advanced
        regression methods.
    Given Input:
        hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and
        scores = [50, 55, 60, 65, 70, 75, 80, 82, 88, 95]
    Expected Output:
        Slope, intercept, and predicted score for 8 hours of study.
    """
    logger.info(f"Exercise 29: Linear Regression to Predict Scores")
    pass



#########################################################################################
def exercise_30_z_score_outlier_detection():
    """
    Exercise 30: Z-Score Outlier Detector Combining NormalDist and quantiles()
    Problem Statement:
        Write a Python function that combines statistics.NormalDist and
        statistics.quantiles() to build a dual-method outlier detector: one
        based on z-scores from the fitted normal distribution, and one based
        on the IQR fence method, then compares which values each method flags.
    Purpose:
        No single outlier detection method is universally best. The z-score
        method assumes normality and is sensitive to extreme values distorting
        the mean and standard deviation. The IQR method is non-parametric
        and robust to skew. Combining both in a single function and comparing
        their outputs builds the critical thinking needed to choose the right
        tool for a given dataset in real data cleaning pipelines.
    Given Input:
        data = [14, 18, 11, 13, 6, 8, 2, 74, 12, 9, 17, 15, 10, 13, 16, 8, 11, -5, 14, 12]
    Expected Output:
        Outliers flagged by each method printed separately,
        followed by a comparison showing agreements and disagreements.
    """
    logger.info(f"Exercise 30: Z-Score Outlier Detector Combining NormalDist and quantiles()")
    pass

