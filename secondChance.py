import copy


class Node:
    pageId = -1
    accessFlag = 0
    noPageFlag = 0

    def __init__(self, pageId, accessFlag, noPageFlag):
        self.pageId = pageId
        self.accessFlag = accessFlag
        self.noPageFlag = noPageFlag


class Request:
    requestId = 0
    frames = []
    fifo = []
    pageId = -1

    def __init__(self, pageId, frames, fifo, requestId):
        self.requestId = requestId
        self.pageId = pageId
        self.frames = copy.deepcopy(frames)
        self.fifo = copy.deepcopy(fifo)


class SecondChance:
    framesCount = 0
    requests = []
    out = []
    noPageCount = 0

    def __init__(self, framesCount, requests):
        self.requests = requests
        self.framesCount = framesCount

    def DoMagic(self):
        # set self values to default
        self.out = []
        self.noPageCount = 0

        # just do the job
        requestId = 0
        for pageId in self.requests:
            frames = []
            fifo = []
            requestId += 1

            # initialize new table
            if len(self.out) == 0:
                fifo.append(pageId)
                newNode = Node(pageId, 1, 1)
                self.noPageCount += 1
                frames.append(copy.deepcopy(newNode))
                newRequest = Request(pageId, frames, fifo, requestId)
                self.out.append(copy.deepcopy(newRequest))
                continue

            # now the play begins

            lastRequest = self.out[-1]
            # when there is some free frames
            if len(lastRequest.frames) < self.framesCount:
                fifo = copy.deepcopy(lastRequest.fifo)
                frames = copy.deepcopy(lastRequest.frames)
                for page in frames:
                    page.noPageFlag = 0

                for page in frames:
                    if page.pageId == pageId:
                        break
                else:
                    newNode = Node(pageId, 1, 1)
                    fifo.append(pageId)
                    self.noPageCount += 1
                    frames.append(copy.deepcopy(newNode))

                newRequest = Request(pageId, frames, fifo, requestId)
                self.out.append(copy.deepcopy(newRequest))
                continue
            # end of if

            # first - check if all of pages has access flag - if true, unset them all the flag
            fifo = copy.deepcopy(lastRequest.fifo)
            frames = copy.deepcopy(lastRequest.frames)

            for page in frames:
                page.noPageFlag = 0

            # now look for page in frames - if exists there is no point to put it there again
            for page in frames:
                if page.pageId == pageId:
                    page.accessFlag = 1
                    newRequest = Request(pageId, frames, fifo, requestId)
                    self.out.append(copy.deepcopy(newRequest))
                    break
            else:

                flagCount = 0
                for page in frames:
                    if page.accessFlag:
                        flagCount += 1
                # we know how many nodes has access flag, let's compare it with amount of frames
                # if every one has second chance - lets grab them it
                if flagCount >= self.framesCount:
                    for page in frames:
                        page.accessFlag = 0

                # now go through fifo stack
                i = -1
                while i < self.framesCount:
                    i += 1
                    page = fifo[i]
                    # now get flag of this page
                    pageFlag = 0
                    for node in frames:
                        if node.pageId == page:
                            pageFlag = node.accessFlag
                            break

                    # pop front of stack, push on back new value, add new value to table
                    if pageFlag == 0:
                        fifo.pop(0)
                        fifo.append(pageId)
                        for node in frames:
                            if node.pageId == page:
                                node.pageId = pageId
                                node.accessFlag = 1
                                node.noPageFlag = 1
                                self.noPageCount += 1
                                break
                        break
                    # grab second chance
                    if pageFlag == 1:
                        for node in frames:
                            if node.pageId == page:
                                node.accessFlag = 0
                                break
                        fifo.pop(0)
                        fifo.append(page)
                        i -= 1
                        continue
                # end of loop
                newRequest = Request(pageId, frames, fifo, requestId)
                self.out.append(copy.deepcopy(newRequest))
        # end of loop

    # there is edge of magic world ;(

    def GetOutput(self):
        outputStr = "Braków stron: {0} \n".format(
            self.noPageCount)

        row = "Kwant czasu |  "
        for request in self.out:
            if request.requestId < 10:
                tmp = str(request.requestId) + " "
            else:
                tmp = str(request.requestId)
            row += tmp + "  |  "

        n = len(row)

        outputStr += "\n" + row

        rowDelimiter = ""
        for i in range(0, n-2):
            rowDelimiter += "_"

        outputStr += "\n"+rowDelimiter

        outputStr += "\nOdwołanie   |  "
        for request in self.out:
            outputStr += str(request.pageId) + "   |  "

        outputStr += "\n"+rowDelimiter

        # print row for each frame in table
        for frameId in range(1, self.framesCount+1):
            row = ""
            row = "Ramka {0}".format(frameId)
            for n in range(len(row), 10):
                row += " "
            row += "  |"

            for request in self.out:
                tmpRow = ""
                try:
                    page = request.frames[frameId-1]
                except IndexError:
                    page = Node(-1, -1, -1)
                finally:
                    if page.pageId < 1:
                        row += "      |"
                        continue

                    if page.noPageFlag:
                        tmpRow += "*"

                    tmpRow += str(page.pageId)

                    if page.accessFlag == 0:
                        tmpRow += "(0)"
                    if page.accessFlag == 1:
                        tmpRow += "(1)"

                    row += "{0: ^6}".format(tmpRow)
                    row += "|"
            # end of for

            row += "\n" + rowDelimiter
            outputStr += "\n" + row

        # end of for

        # now print fifo stack
        for frameId in range(1, self.framesCount+1):
            row = "            |  "
            for request in self.out:
                try:
                    page = request.fifo[frameId-1]
                    page = str(page)
                except IndexError:
                    page = " "
                finally:
                    row += page + "   |  "
            outputStr += "\n" + row
        # end of nested for

        return outputStr
    # end of GetOutput()


def algorytm_drugiej_szansy(_framesCount, _requestCount, _requests):
    result = SecondChance(requests=_requests, framesCount=_framesCount)
    result.DoMagic()
    print(result.GetOutput())
