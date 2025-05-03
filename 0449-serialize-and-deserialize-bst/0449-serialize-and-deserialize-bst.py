class Codec:

    def serialize(self, root):
        res = []
        def solut(node):
            if not node:
                res.append('x')
                return
            res.append(str(node.val))
            solut(node.left)
            solut(node.right)
        solut(root)
        return ' '.join(res)

    def deserialize(self, data):
        def dfs(nodes):
            val = next(nodes)
            if val == 'x':
                return None
            node = TreeNode(int(val))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node
        return dfs(iter(data.split()))