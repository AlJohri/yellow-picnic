# Yellow Picnic Analyzer

Analyze and score weekly [Yellow Picnic](https://yellowpicnic.com) meals by macro ratios.

## Prerequisites

- [Install mise](https://mise.jdx.dev/getting-started.html)
- Sign into [yellowpicnic.com](https://yellowpicnic.com) in Chrome — we use [browser_cookie3](https://github.com/borisbabic/browser_cookie3) to read cookies from Chrome

## Quick Start

```bash
mise run all
```

## Example Output

```
$ mise run all
Downloaded to 2026-02-15/page.html (383452 bytes)
Wrote 19 meals to 2026-02-15/data.json
                                   name  calories  protein  carbs  fat  protein_to_carbs  protein_to_fat  score
YP Signature - Chipotle Chicken Burrito       563       51     45   18              1.13            2.83   1.37
               Parmesan Crusted Chicken       435       41     28   17              1.46            2.41   1.34
                 Mango Habanero Chicken       439       39     27   18              1.44            2.17   1.26
                        Chicken Lo Mein       492       45     35   20              1.29            2.25   1.23
                          Pollo Guisado       439       38     33   16              1.15            2.38   1.22
                 Creamy Tuscan Rigatoni       554       48     50   20              0.96            2.40   1.16
                  Creamy Cowboy Chicken       495       43     30   23              1.43            1.87   1.15
                 Blackened Chicken Bowl       486       40     41   17              0.98            2.35   1.15
                   Sweet & Sour Chicken       513       41     44   18              0.93            2.28   1.11
           Chicken Breakfast Quesadilla       446       29     45   15              0.64            1.93   0.88
                       Pastelon de Papa       456       32     24   28              1.33            1.14   0.87
     Chimichurri Steak Alfredo Rigatoni       536       35     41   25              0.85            1.40   0.78
                       Bang Bang Salmon       449       28     25   26              1.12            1.08   0.77
                    Lemon Garlic Shrimp       496       29     33   26              0.88            1.12   0.70
                 Vanilla Overnight Oats       458       23     52   18              0.44            1.28   0.59
                      Black Bean Burger       436       21     41   21              0.51            1.00   0.52
  Dark Chocolate Raspberry French Toast       483       19     57   19              0.33            1.00   0.46
                 Chickpea & Maduro Stew       464       15     73   14              0.21            1.07   0.44
                          Eggplant Parm       480       18     44   29              0.41            0.62   0.36
```
