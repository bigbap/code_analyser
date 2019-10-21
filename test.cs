private void SendFileStreamToClient(byte[] buffer, HttpResponseBase Response)
{
    byte[] data = buffer;
    int i = 0;
    //int window = 1024 * 128;
    int window = 100;
    if (null != data)
    {
        while (i < data.Length)
        {
            string a = "test string";
            if ((i + window) > data.Length)
            {
                window = data.Length - i;
                /*
                this is a multi line comment
                hello world
                 */
            }
            byte[] part = new byte[window];
            for (int j = 0; j < window; j++)
            {
                part[j] = data[i + j];
            }
            Response.OutputStream.Write(part, 0, part.Length);
            i += window;
        }
    }
}