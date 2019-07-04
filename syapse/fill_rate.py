"""
Assignment for Syapse

Simple fillrate/sparsity reporter,
optimized for memory footprint since csv files could be very large
"""
import csv
import os
import sys
from collections import defaultdict


def not_null(item):
    """
    Some validations
    """
    return item != '' and item != 'NULL' and item != 'null' and item != 'none'


class DataValidator:
    """
    Validates provided directory for sparsity and produce report
    """

    def __init__(self, directory_name):
        self.directory_name = directory_name
        self.file_fill_rates = defaultdict(lambda: defaultdict(int))
        self.global_fill_rates = defaultdict(int)
        self.number_of_records_per_file = defaultdict(int)
        self.records_per_feature = defaultdict(int)

    def print_file_report(self, filename):
        """
        Prints report based on filename
        :param filename: filename to print report for
        """
        print('Report for file: {}'.format(filename))
        for feature in self.file_fill_rates[filename]:
            fill_rate = self.file_fill_rates[filename][feature] / self.number_of_records_per_file[filename]
            print('Filename: {}, {:.2%}'.format(filename, 1 - fill_rate))

    def print_global_report(self):
        """
        Prints global report for all features
        """
        for feature in self.global_fill_rates:
            fill_rate = self.global_fill_rates[feature] / self.records_per_feature[feature]
            print("Sparsity for feature {} is {:.2%}".format(feature, 1 - fill_rate))

    def print_report(self):
        """
        Prints combined report
        """
        for filename in self.number_of_records_per_file:
            self.print_file_report(filename)
        self.print_global_report()

    def calculate_fillrate(self, filename):
        with open(os.path.join(self.directory_name, filename)) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.number_of_records_per_file[filename] += 1
                for key in row:
                    self.records_per_feature[key] += 1
                    if not_null(row[key]):
                        self.file_fill_rates[filename][key] += 1
                        self.global_fill_rates[key] += 1

    def make_report(self):
        for filename in os.listdir(self.directory_name):
            if filename.endswith('.csv'):
                self.calculate_fillrate(filename)


if __name__ == '__main__':
    validator = DataValidator(os.path.dirname(sys.argv[0]))
    validator.make_report()
    validator.print_report()
