import logging
import statistics
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
    data = [4, 7, 13, 2, 19, 25, 8, 14, 3, 31, 11, 6, 17, 22, 9, 5, 28, 16, 10, 100]
    # Compute quartiles (n=4 gives [Q1, Q2, Q3])
    quantiles = statistics.quantiles(data, n=4)
    q1, q2, q3 = quantiles
    iqr = q3 - q1
    lower_fence = q1 - (1.5 * iqr)
    upper_fence = q3 + (1.5 * iqr)
    outliers = [num for num in data if num <= lower_fence or num >= upper_fence]
    logger.info(f"  Raw data (sorted lowest to highest): {sorted(data)}")
    logger.info(f"  Quantiles                          : {quantiles}")
    logger.info(f"  Lower Fence (Q1 - 1.5×IQR)         : {lower_fence}")
    logger.info(f"  Q1 (25th percentile)               : {q1}")
    logger.info(f"  Q2 (50th percentile)               : {q2}")
    logger.info(f"  Q3 (75th percentile)               : {q3}")
    logger.info(f"  IQR (Q3 - Q1)                      : {iqr}")
    logger.info(f"  Upper Fence (Q3 + 1.5×IQR)         : {upper_fence}")
    logger.info(f"  Outliers (IQR Method)              : {outliers}")
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
    Additional info:
        statistics.harmonic_mean(data): Computes n / (1/x1 + 1/x2 + ... + 1/xn),
        which is the reciprocal of the arithmetic mean of the reciprocals.
    """
    logger.info(f"Exercise 22: Harmonic Mean of Internet Speeds")
    speeds = [10, 20, 40, 80]
    harmonic_mean = statistics.harmonic_mean(speeds)
    arithmetic_mean = statistics.mean(speeds)
    logger.info(f"  Speeds (Mbps)    : {speeds}")
    logger.info(f"  Harmonic mean    : {harmonic_mean:.2f} Mbps")
    logger.info(f"  Arithmetic mean  : {arithmetic_mean:.2f} Mbps")
    # Manual verification of harmonic mean formula
    n = len(speeds)
    manual_harmonic = n / sum(1 / s for s in speeds)
    logger.info(f"  Manual harmonic  : {manual_harmonic:.2f} Mbps")
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
    growth_factors = [1.08, 0.95, 1.12, 1.06, 0.98]
    years = len(growth_factors)
    geo_mean = statistics.geometric_mean(growth_factors)
    arith_mean = statistics.mean(growth_factors)
    manual_compunding = math.prod(growth_factors)
    geo_mean_compounded = geo_mean ** len(growth_factors)
    arith_mean_compounded = arith_mean ** len(growth_factors)
    initial_investment = 1000
    # Final portfolio value
    actual_final = initial_investment * manual_compunding
    geo_projected = initial_investment * (geo_mean ** years)
    arith_proj = initial_investment * (arith_mean ** years)

    final_investment = initial_investment * geo_mean_compounded
    final_investment_arith = initial_investment * arith_mean_compounded
    logger.info(f"  Initial investment: {initial_investment}, for a period of {years} years.")
    logger.info(f"  Geometric mean (CAGR)             : {geo_mean:.6f} "
                f"({(geo_mean - 1) * 100:.2f}% per year)")
    logger.info(f"  Arithmetic mean                   : {arith_mean:.6f} "
                f"({(arith_mean - 1) * 100:.2f}% per year)")
    logger.info(f"  Geometric mean (CAGR) compounded  : {geo_mean_compounded:.6f} ")
    logger.info(f"  Total cumulative growth (manual)  : {manual_compunding:.6f} ")
    logger.info(f"  Arithmetic mean compounded        : {arith_mean_compounded:.6f} ")
    logger.info(f"  ---------------------------")
    logger.info(f"  Initial investment                : {initial_investment:.2f} ")
    logger.info(f"  Investment value after compounding: {actual_final:.2f}")
    logger.info(f"  Predicted value geometric mean    : {final_investment:.2f}")
    logger.info(f"  Predicted value arithmetic mean   : {final_investment_arith:.2f}")
    logger.info("")
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
    hours = [2, 4, 6, 8, 5, 7, 3, 9, 1, 6]
    scores = [55, 70, 80, 92, 74, 85, 60, 95, 45, 78]
    mean_hours = statistics.mean(hours)
    mean_scores = statistics.mean(scores)
    sample_covariance = statistics.covariance(hours, scores)
    manual_result = sum((xi - statistics.mean(hours)) * (yi - statistics.mean(scores))
                          for xi, yi in zip(hours, scores)) / (len(hours) - 1)

    logger.info(f"  Hours studied                                : {hours}")
    logger.info(f"  Test scores                                  : {scores}")
    logger.info(f"  Mean hours                                   : {mean_hours:.2f}")
    logger.info(f"  Mean score                                   : {mean_scores:.2f}")
    logger.info(f"  Sample Covariance using statistics.covariance: {sample_covariance:.2f}")
    logger.info(f"  Expected Covariance using manual calculation : {manual_result:.2f}")
    logger.info(f"  Results match                                : "
                f"{math.isclose(sample_covariance, manual_result)}")
    # Interpret the sign
    message = "Interpretation: Zero covariance - no linear relationship detected."
    if sample_covariance > 0:
        message = "Interpretation: Positive covariance - more hours studied tends to mean higher scores."
    elif sample_covariance < 0:
        message = "Interpretation: Negative covariance - more hours studied tends to mean lower scores."
    logger.info(f"  {message}")
    # Limitation: covariance is scale-dependent
    logger.info(f"  Limitation: covariance is {sample_covariance:.2f} for hours vs scores.")
    logger.info(f"  This number is hard to interpret in isolation because it depends on the")
    logger.info(f"  units and scale of both variables. Use correlation (Exercise 25) to normalise it.")
    logger.info("")
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

    # Interpret strength and direction
    def interpret_r(r):
        abs_r = abs(r)
        direction = "positive" if r > 0 else "negative"
        if abs_r >= 0.9:
            strength = "very strong"
        elif abs_r >= 0.7:
            strength = "strong"
        elif abs_r >= 0.5:
            strength = "moderate"
        elif abs_r >= 0.3:
            strength = "weak"
        else:
            strength = "very weak or no"
        return f"{strength} {direction} linear relationship"

    logger.info(f"Exercise 25: Pearson Correlation Coefficient")
    hours = [2, 4, 6, 8, 5, 7, 3, 9, 1, 6]
    scores = [55, 70, 80, 92, 74, 85, 60, 95, 45, 78]
    r = statistics.correlation(hours, scores)
    cov = statistics.covariance(hours, scores)
    std_hours = statistics.stdev(hours)
    std_scores = statistics.stdev(scores)
    r_manual = (cov / (std_hours * std_scores))

    logger.info(f"  Hours studied            : {hours}")
    logger.info(f"  Test scores              : {scores}")
    logger.info(f"  Pearson r                : {r:.4f}")
    logger.info(f"  Interpretation           : {interpret_r(r)}")
    logger.info(f"  -------------------- Manual verification --------------------")
    logger.info(f"  covariance(hours, scores): {cov:.4f}")
    logger.info(f"  stdev(hours)             : {std_hours:.4f}")
    logger.info(f"  stdev(scores)            : {std_scores:.4f}")
    logger.info(f"  cov / (std_h * std_s)    : {r_manual:.4f}")
    logger.info(f"  Matches correlation()    : "
                f"{math.isclose(r, r_manual)}")
    logger.info("")
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
    mu = 70
    sigma = 10
    low_score = 60
    high_score = 85
    lower_range = 65
    upper_range = 80
    dist = statistics.NormalDist(mu, sigma)
    above_average = (1 - dist.cdf(high_score))
    below_average = dist.cdf(low_score)
    within_range = (dist.cdf(upper_range) - dist.cdf(lower_range))
    logger.info(f"  Distribution      : N(mu={dist.mean}, sigma={dist.stdev})")
    logger.info(f"  Variance          : {dist.variance}")
    logger.info(f"  P(score > {high_score})     : "
                f"{above_average:.4f} ({above_average * 100:.2f}%).")
    logger.info(f"  P(score < {low_score})     : "
                f"{below_average:.4f} ({below_average * 100:.2f}%).")
    logger.info(f"  P({lower_range} < score < {upper_range}): "
                f"{within_range:.4f} ({within_range * 100:.2f}%).")
    logger.info("")
    # Verify empirical rule (68-95-99.7)
    p_1sigma = dist.cdf(dist.mean + dist.stdev) - dist.cdf(dist.mean - dist.stdev)
    p_2sigma = dist.cdf(dist.mean + 2 * dist.stdev) - dist.cdf(dist.mean - 2 * dist.stdev)
    p_3sigma = dist.cdf(dist.mean + 3 * dist.stdev) - dist.cdf(dist.mean - 3 * dist.stdev)
    logger.info(f"  ---------------- Empirical rule verification ----------------")
    logger.info(f"  Within 1 sigma (60-80)  : {p_1sigma * 100:.2f}%  (expected ~68.27%)")
    logger.info(f"  Within 2 sigma (50-90)  : {p_2sigma * 100:.2f}%  (expected ~95.45%)")
    logger.info(f"  Within 3 sigma (40-100) : {p_3sigma * 100:.2f}%  (expected ~99.73%)")
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

    def interpret_overlap(ov):
        if ov >= 0.85:
            return "Very high overlap - distributions are nearly indistinguishable."
        elif ov >= 0.60:
            return "Moderate overlap - some separation but not conclusive."
        elif ov >= 0.30:
            return "Low overlap - distributions are meaningfully different."
        else:
            return "Very low overlap - distributions are clearly distinct."

    logger.info(f"Exercise 27: Distribution Overlap Between Two Models")
    model_a = statistics.NormalDist(mu=0.15, sigma=0.03)
    model_b = statistics.NormalDist(mu=0.22, sigma=0.04)
    overlap = model_a.overlap(model_b)
    symmetric_overlap = (model_a.overlap(model_b) == model_b.overlap(model_a))
    logger.info(f"  Interpretation    : {interpret_overlap(overlap)}")
    logger.info(f"  Model A Distribution      : N(mu={model_a.mean}, sigma={model_a.stdev})")
    logger.info(f"  Model A Variance          : {model_a.variance}")
    logger.info(f"  Model B Distribution      : N(mu={model_b.mean}, sigma={model_b.stdev})")
    logger.info(f"  Model B Variance          : {model_b.variance}")

    logger.info(f"  Overlap Coefficent Models A and B: {overlap:.4f} ({overlap * 100:.1f}%)")
    logger.info(f"  Interpretation            : {interpret_overlap(overlap)}")
    # Symmetry check
    logger.info(f"  Symmetry check            : model_b.overlap(model_a) = {model_b.overlap(model_a):.4f}")
    logger.info(f"  Symmetric                 : {abs(overlap - model_b.overlap(model_a)) < 1e-12}")
    logger.info("")
    logger.info(f"  ---------------- Edge Cases ----------------")

    model_c_close = model_a
    logger.info(f"  Model C Distribution      : N(mu={model_c_close.mean}, sigma={model_c_close.stdev})")
    logger.info(f"  Model C Variance          : {model_c_close.variance}")
    overlap_c_and_a = model_c_close.overlap(model_a)
    logger.info(f"  Overlap Coefficent Models A and C: {overlap_c_and_a:.4f} ({overlap_c_and_a * 100:.1f}%)")
    logger.info(f"  Interpretation            : {interpret_overlap(overlap_c_and_a)}")

    model_y_apart = statistics.NormalDist(mu=0.80, sigma=0.24)
    logger.info(f"  Model Y Distribution      : N(mu={model_y_apart.mean}, sigma={model_y_apart.stdev})")
    logger.info(f"  Model Y Variance          : {model_y_apart.variance}")
    overlap_y_and_a = model_y_apart.overlap(model_a)
    logger.info(f"  Overlap Coefficent Models Y and A: {overlap_y_and_a:.4f} ({overlap_y_and_a * 100:.1f}%)")
    logger.info(f"  Interpretation            : {interpret_overlap(overlap_y_and_a)}")
    logger.info("")
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
    raw_scores = [52, 61, 47, 73, 68, 55, 80, 44, 66, 71, 58, 49, 76, 63, 57]
    dist = statistics.NormalDist.from_samples(raw_scores)
    target_mean = 75
    offset = target_mean - dist.mean
    revised_scores = []
    for grade in raw_scores:
        revised_scores.append(float(f"{grade + offset:.1f}"))
    revised_dist = statistics.NormalDist.from_samples(revised_scores)
    logger.info(f"  Original scores     : {sorted(raw_scores)}")
    logger.info(f"  Fitted mean         : {dist.mean:.2f}")
    logger.info(f"  Fitted stdev        : {dist.stdev:.2f}")
    logger.info(f"  Target mean         : {target_mean:.2f} ")
    logger.info(f"  Shift applied       : {offset:.2f} points")
    logger.info(f"  Curved scores       : {sorted(revised_scores)}")
    logger.info(f"  New mean            : {revised_dist.mean:.2f}")
    logger.info(f"  New stdev           : {revised_dist.stdev:.2f}")
    logger.info(f"")
    # Side-by-side comparison
    logger.info(f"  {'Raw':>6} | {'Curved':>8} | {'Change':>8}")
    logger.info(f"  ----------------------------")
    for raw, curved in sorted(zip(raw_scores, revised_scores)):
        logger.info(f"  {raw:>6} | {curved:>8} | {curved - raw:>+8.1f}")

    # Probability of failing (score < 60) before and after the curve
    p_fail_raw = dist.cdf(60)
    p_fail_curved = revised_dist.cdf(60)
    logger.info(f"  P(score < 60) before curve : {p_fail_raw * 100:.1f}%")
    logger.info(f"  P(score < 60) after curve  : {p_fail_curved * 100:.1f}%")
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
    logger.info("")
    logger.info(f"Exercise 29: Linear Regression to Predict Scores")
    hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    scores = [50, 55, 60, 65, 70, 75, 80, 82, 88, 95]
    hours_scores_curve = statistics.linear_regression(hours, scores)
    slope = hours_scores_curve.slope
    intercept = hours_scores_curve.intercept
    hours_for_prediction = 8

    logger.info(f"  Hours  : {hours}")
    logger.info(f"  Scores : {scores}")
    logger.info("")
    logger.info(f"  Regression line  : score = {slope:.4f} × hours + {intercept:.4f}")
    logger.info(f"  Slope            : {slope:.4f}  (each extra hour adds ~{slope:.1f} points)")
    logger.info(f"  Intercept        : {intercept:.4f}  (predicted score at 0 hours)")
    logger.info(f"  Predicted score for {hours_for_prediction} hours: "
                f"{((slope * hours_for_prediction) + intercept):.2f}")

    predicted_scores = []
    residuals = []
    for hour, score in zip(hours, scores):
        predicted_score = (slope * hour) + intercept
        predicted_scores.append(predicted_score)
        residuals.append(score - predicted_score)

    # Detailed analysis
    logger.info(f"  {'Hours':>6} | {'Score':>8} | {'Predicted':>8} | {'Residual':>8}")
    logger.info(f"  ----------------------------------------")
    for h, s, ps, res in sorted(zip(hours, scores, predicted_scores, residuals)):
        logger.info(f"  {h:>6} | {s:>8} | {ps:>+8.2f} | {res:>8.2f}")
    logger.info("")

    # R-squared from regression vs correlation
    r = statistics.correlation(hours, scores)
    r_sq = r ** 2
    logger.info(f"  R² (from correlation) : {r_sq:.4f}  ({r_sq * 100:.1f}% of variance explained)")
    logger.info("")
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

    def calculate_distribution_using_quantiles(input_data):
        # Compute quartiles (n=4 gives [Q1, Q2, Q3])
        quantiles = statistics.quantiles(input_data, n=4)
        q1, q2, q3 = quantiles
        iqr = q3 - q1
        lower_fence = q1 - (1.5 * iqr)
        upper_fence = q3 + (1.5 * iqr)
        outliers = [num for num in data if num <= lower_fence or num >= upper_fence]
        logger.info(f"  Raw data (sorted lowest to highest): {sorted(data)}")
        logger.info(f"  IQR Method (Q1 = {q1}, Q2 = {q2}, Q3 = {q3})")
        logger.info(f"  Lower Fence (Q1 - 1.5×IQR)         : {lower_fence:.2f}")
        logger.info(f"  Upper Fence (Q3 + 1.5×IQR)         : {upper_fence:.2f}")
        logger.info(f"  IQR Outliers                       : {outliers}")
        return outliers

    def calculate_distribution_using_z_scores(input_data, threshold):
        dist = statistics.NormalDist.from_samples(input_data)
        zscores = []
        raw_zscores = []
        outliers = []
        for item in input_data:
            raw_zscores.append(dist.zscore(item))
            current_item_zscore = float(f"{dist.zscore(item):.4f}")
            zscores.append(current_item_zscore)
        results = zip(input_data, zscores)

        logger.info("------------------------------------------------------")
        logger.info(f"  --- Method 1: Z-score using NormalDist ---")
        logger.info(f"  Raw data (sorted lowest to highest): {data}")
        logger.info(f"  Fitted mean      : {dist.mean:.2f}")
        logger.info(f"  Fitted stdev     : {dist.stdev:.2f}")
        logger.info(f"  Z-score method (|z| > {threshold}):")

        for score, zscore in list(results):
            if abs(zscore) > threshold:
                flag = " <-- OUTLIER"
                outliers.append(score)
            else:
                flag = ""
            logger.info(f"  {score:>5}  z = {zscore:+.2f}{flag}")


        # Calculate the mean and standard deviation manually...
        mean = sum(input_data) / len(input_data)
        # Calculate the standard deviation
        differences = [(value - mean) ** 2 for value in input_data]
        sum_of_differences = sum(differences)
        standard_deviation = (sum_of_differences / (len(input_data) - 1)) ** 0.5
        # Calculate the z-scores manually
        zscores_manual = [(value - mean) / standard_deviation for value in input_data]
        zscores_match = (zscores_manual == raw_zscores)
        logger.info(f"  zscores from distribution match manual zscores: {zscores_match}")
        logger.info("")
        return outliers

    data = [14, 18, 11, 13, 6, 8, 2, 74, 12, 9, 17, 15, 10, 13, 16, 8, 11, -5, 14, 12]
    zscore_outliers = calculate_distribution_using_z_scores(sorted(data), 2.5)
    iqr_outliers = calculate_distribution_using_quantiles(sorted(data))
    found_in_both_sets = set(zscore_outliers) & set(iqr_outliers)
    found_in_zscore_only = set(zscore_outliers) - set(iqr_outliers)
    found_in_iqr_only = set(iqr_outliers) - set(zscore_outliers)
    scores_within_range = set(data) - (set(found_in_zscore_only) |
                                       set(found_in_iqr_only) |
                                       set(found_in_both_sets))
    logger.info("")
    logger.info(f"  ---------- Outlier Analysis ----------")
    logger.info(f"  Flagged by BOTH methods    : {sorted(found_in_both_sets)}")
    logger.info(f"  Z-score only               : {sorted(found_in_zscore_only)}")
    logger.info(f"  IQR only                   : {sorted(found_in_iqr_only)}")
    logger.info(f"  Clean data (neither method): {sorted(scores_within_range)}")
    pass

