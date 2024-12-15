from workers.app_worker import yt_download_video_task

# result = add.delay(4, 4)
# print(result.get())


# ret2 = (add.s(1, 2) | add.si(3,30)).apply_async()
# ret = (add.s(1, 2) | add.s(3)).apply_async()

# print(ret.get())
# print(ret2.get())

task_dl_result = yt_download_video_task.apply_async(args=["https://www.youtube.com/shorts/tFKdZPvyOc8?feature=share"])