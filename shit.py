from workers.app_worker import yt_download_video_task, whisper_transcribe

# result = add.delay(4, 4)
# print(result.get())


# ret2 = (add.s(1, 2) | add.si(3,30)).apply_async()
# ret = (add.s(1, 2) | add.s(3)).apply_async()

# print(ret.get())
# print(ret2.get())



# task_dl_result = yt_download_video_task.apply_async(args=["https://www.youtube.com/shorts/tFKdZPvyOc8?feature=share"])
# task_dl_result.get()


res = (yt_download_video_task.s("https://www.youtube.com/watch?v=VGL3RVzaTYA") 
       | whisper_transcribe.s()).apply_async()
print(res.get())

# res = (whisper_transcribe.s("d7753b76-b381-4ce0-81dc-cca16f1798d8")).apply_async()
# print(res.get())
