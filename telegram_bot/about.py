def static_about(bot, call):
    bot.send_message(
        call.message.chat.id,
        """
        [Reverse Code](https://pypi.org/project/inverse-code/) is a library created for Python to help developers encrypt and retrieve their data in a simple and dynamic way.\n
        This cryptography is at least vaguely similar to real-world things, such as Reed-Solomon error correction codes or some interspersed data formats that can be transmitted by IoT edge devices.\n
        ASCII, means American standard code for information exchange. It is a 7 -bit character code where each individual bit represents a unique character.\n
        I used the 8-bit ASCII table with 256 characters and symbols, which is based on the Windows-1252 characters set. \n
        """,
    )
