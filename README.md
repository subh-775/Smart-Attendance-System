# Smart Attendance System with Face Recognition and OpenCV

## Workflow

* **Image Capture:** The system uses a camera to take input and matches it with available databases.
* **Face Recognition:** Deep learning algorithms analyze these images to identify and verify the identities of the people present. The system compares the captured faces with a database of known individuals.
* **Attendance Tracking:** When a recognized face is detected, the system records the attendance. It can create a log or store the data in a spreadsheet.
* **Real-Time Processing:** The entire process happens in real-time, allowing for efficient and accurate attendance management.

## Installing Dependencies

1.  Clone the Dlib repository from GitHub:
    ```bash
    git clone [https://github.com/z-mahmud22/Dlib_Windows_Python3.x.git](https://github.com/z-mahmud22/Dlib_Windows_Python3.x.git)
    ```

2.  Install a compatible version of numpy:
    ```bash
    pip install numpy==1.26.0
    ```

3.  Install the face-recognition library:
    ```bash
    pip install face-recognition
    ```
## How the system actually works:
1. Store images of known users in the users directory, ensuring filenames correspond to their names.
2. The system captures live video and calculates facial encodings for any detected faces.
3. Calculated encodings are matched against the directory; successful matches are identified and logged on screen.

## License

```bash
Apache License 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

