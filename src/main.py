from textnode import TextNode, TextType

def main():
    dummy_node = TextNode("dummy text", TextType.LINK, "https://boot.dev")
    print(dummy_node)

main()